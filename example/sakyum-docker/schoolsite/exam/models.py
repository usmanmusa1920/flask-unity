# from sakyum software, your app (exam) models.py file
from datetime import datetime
from sakyum.contrib import db


"""
when ever you create a model, make sure you import it in your project config.py
file and register it to the admin page in other to see it in admin page
"""

class ExamQuestionModel(db.Model):
  """ Exam default Question model """
  id = db.Column(db.Integer, primary_key=True)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  # the user field is the user who create the question and he is in the `User` models of auth
  user = db.relationship("User", backref="user")
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  question_text = db.Column(db.Text, nullable=False)
  choices = db.relationship('ExamChoiceModel', backref='selector', lazy=True)

  def __str__(self):
    return f"{self.question_text}"

  def __repr__(self):
    return f"{self.question_text}"
    
  # the `ExamChoiceModel` is the choice model class below
  # the `selector` is the attribute that we can use to get selector who choose the choice
  # the `lazy` argument just define when sqlalchemy loads the data from the database


class ExamChoiceModel(db.Model):
  """ Exam default Choice model """
  id = db.Column(db.Integer, primary_key=True)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  question_id = db.Column(db.Integer, db.ForeignKey('exam_question_model.id'), nullable=False)
  # you can pass a keyword argument of `unique=True` in the below choice_text field
  # that will make it unique across the entire table of choice
  choice_text = db.Column(db.String(100), nullable=False)

  def __str__(self):
    return f"{self.choice_text}"

  def __repr__(self):
    return f"{self.choice_text}"
