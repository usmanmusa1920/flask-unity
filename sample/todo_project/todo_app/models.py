# from sakyum software, your app (todo_app) models.py file
from datetime import datetime
from todo_project.config import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    
    # the `Post` is the post model class below
    # the `author` is the attribute that we can use to get author who created the post
    # the `lazy` argument just define when sqlalchemy loads the data from the database

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
# db.create_all()


# move on to terminal and paste the following command
# python
# from zaria.config import db
# db.create_all()

# from blogy.models import User, Post
# u = User(username="user_1", email="user_1@email.com", password="1234")
# p = Post(title="post one", content="Lorem lipsum doler", user_id=u.id)

# db.session_add(u)
# db.session_add(p)
# db.commit()

# User.query.all() # show all users
# Post.query.all() # show all post of users

# dir(User.query) # to see many other method
