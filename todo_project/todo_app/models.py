# from sakyum software, your app (todo_app) models.py file
from datetime import datetime
from todo_project.config import db

"""
when ever you create a model, make sure you import it in your
project config.py file before you run your application to avoid error
"""

# class User(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   username = db.Column(db.String(20), unique=True, nullable=False)
#   email = db.Column(db.String(120), unique=True, nullable=False)
#   image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
#   password = db.Column(db.String(60), nullable=False)
#   posts = db.relationship('Post', backref='author', lazy=True)
  
#   the `Post` is the post model class below
#   the `author` is the attribute that we can use to get author who created the post
#   the `lazy` argument just define when sqlalchemy loads the data from the database


# class Post(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   title = db.Column(db.String(100), nullable=False)
#   date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#   content = db.Column(db.Text, nullable=False)
#   user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class TodoListModel(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False, unique=True)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  content = db.Column(db.Text, nullable=False)

  def __repr__(self):
    return f"Todo list of ('{self.name}', '{self.date_posted}')"


# move on to terminal and paste the following command, ( in python interpreter )
# make sure you are within that your virtual environment

# from todo_project.config import db
# from todo_app.models import TodoListModel

# db.create_all() # method to create the tables and database
# r = TodoListModel(name='sakyum', content='An extension of flask web framework')

# db.session_add(r)
# db.commit()
# TodoListModel.query.all()

# dir(TodoListModel.query) # to see many other method
