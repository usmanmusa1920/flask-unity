
def _html(name, static_url=None, is_what=True, f="{{", l="}}"):
    if is_what:
        _is = "application"
        static_url = name
    else:
        _is = "project"
        static_url = "base"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" type="text/css" href="{f} url_for('{static_url}.static', filename='style.css') {l}">
  <script type="text/javascript" src="{f} url_for('{static_url}.static', filename='index.js') {l}"></script>
  <title>{name} - index page</title>
</head>
<body>
  <!-- Hello world HTML index -->
  
  <h1>Welcome to flaskey {name} ({_is})</h1>
  <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Numquam quidem in iure architecto, iste eius aperiam, ipsam ducimus commodi soluta ea earum quis eveniet illum fugiat voluptatibus voluptatem aspernatur tenetur?</p>
  
</body>
</html>

"""

_css = r"""/* Hello world CSS index */

body {
  padding: 0;
  margin: 0;
  height: 100vh;
  width: 100vw;
  background: dodgerblue;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

p{
  text-align: center;
}

"""

def _js(name):
    return f"""// Hello world JS index

/* js file */
alert('welcome to {name}')

"""



null = r"""# write awesome code here!
"""

def thunder_dummy(project):
    return f"""from flaskey import boot

if __name__ == "__main__":
    boot()
    
from {project} import app

from {project}.routes import base
app.register_blueprint(base)

# from <app_name>.views import <app_name>
# app.register_blueprint(<app_name>)

app.run(debug=True)
"""



pro_init_dummy = r"""from flask import Flask
app = Flask(__name__)
"""

pro_config_dummy = r"""import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
"""

pro_models_dummy = r"""from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flaskblog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
"""

def pro_routes_dummy(proj):
    return f"""from {proj} import app
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flaskey.utils import template_dir, static_dir
print(template_dir(), static_dir(""))
base = Blueprint("base", __name__, template_folder=template_dir(), static_folder=static_dir(""))

# @base.route('/')
# def index():
#     return "<h1>base index page</h1>"

@base.route('/')
def index():
    return render_template("index.html")
"""


app_init_dummy = r"""
"""

app_routes_dummy = r"""from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm

posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))
"""

app_forms_dummy = r"""from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
"""

app_utils_dummy = r"""
import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)
"""

def app_views_dummy(yourapplication, app):
    return f"""from {yourapplication} import app
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flaskey.utils import template_dir, static_dir
{app} = Blueprint("{app}", __name__, template_folder=template_dir(), static_folder=static_dir("{app}"))

# @{app}.route('/')
# def index():
#     return "<h1>{app} index page</h1>"

@{app}.route('/{app}')
def index():
    return render_template("{app}/index.html")
"""
