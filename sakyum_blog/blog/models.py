# from sakyum software, your app (blog) models.py file
from datetime import datetime
from sakyum_blog.config import db


"""
when ever you create a model, make sure you import it in your
project config.py file in other to see it in admin page
"""

class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  content = db.Column(db.Text, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

  def __repr__(self):
    return f"Post('{self.title}', '{self.date_posted}')"
