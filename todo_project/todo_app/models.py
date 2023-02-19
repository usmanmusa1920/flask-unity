# from sakyum software, your app (todo_app) models.py file
from datetime import datetime
from todo_project.config import db


"""
when ever you create a model, make sure you import it in your
project config.py file in other to see it in admin page
"""


class Todo_appQuestionModel(db.Model):
  """ Todo_app default Question model """
  id = db.Column(db.Integer, primary_key=True)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  # the user field is the user who create the question and he is in the `User` models of auth
  user = db.relationship("User", backref="user")
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  question_text = db.Column(db.Text, nullable=False)
  choices = db.relationship('Todo_appChoiceModel', backref='selector', lazy=True)

  def __str__(self):
    return f"Question {self.id}: {self.question_text}"

  def __repr__(self):
    return f"Question {self.id}: {self.question_text}"
    
  # the `Todo_appChoiceModel` is the choice model class below
  # the `selector` is the attribute that we can use to get selector who choose the choice
  # the `lazy` argument just define when sqlalchemy loads the data from the database


class Todo_appChoiceModel(db.Model):
  """ Todo_app default Choice model """
  id = db.Column(db.Integer, primary_key=True)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  question_id = db.Column(db.Integer, db.ForeignKey('todo_app_question_model.id'), nullable=False)
  # you can pass a keyword argument of `unique=True` in the below choice_text field
  # that will make it unique across the entire table of choice
  choice_text = db.Column(db.String(100), nullable=False)

  def __str__(self):
    return f"{self.choice_text} of {self.question_id}"

  def __repr__(self):
    return f"{self.choice_text} of {self.question_id}"


"""
# *** PLAY WITH API ***

# :move on to terminal and paste the following command,
# :( in python interpreter ) make sure you are within that your virtual environment


from todo_project.config import db
from todo_app.models import Todo_appQuestionModel, Todo_appChoiceModel


# :method to create the tables and database, if it doesn't create db file,
# :run the below command. But if it create just ignore
db.create_all()


q1 = Todo_appQuestionModel(question_text="Is sakyum an extension of flask web framework?")
q2 = Todo_appQuestionModel(question_text="Is flask better with sakyum")

db.session.add(q1)
db.session.add(q2)
db.session.commit()

the_q1 = Todo_appQuestionModel.query.get_or_404(1)
the_q2 = Todo_appQuestionModel.query.get_or_404(2)

c1_1 = Todo_appChoiceModel(choice_text="Yes, it is", question_id=the_q1.id)
c1_2 = Todo_appChoiceModel(choice_text="No, it is not", question_id=the_q1.id)
c1_3 = Todo_appChoiceModel(choice_text="I don't no", question_id=the_q1.id)

c2_1 = Todo_appChoiceModel(choice_text="Yes for sure", question_id=the_q2.id)
c2_2 = Todo_appChoiceModel(choice_text="Always the best", question_id=the_q2.id)
c2_3 = Todo_appChoiceModel(choice_text="All the time", question_id=the_q2.id)

db.session.add(c1_1)
db.session.add(c1_2)
db.session.add(c1_3)

db.session.add(c2_1)
db.session.add(c2_2)
db.session.add(c2_3)

db.session.commit()

# to see all our questions
Todo_appQuestionModel.query.all()
dir(Todo_appQuestionModel.query) # to see many other method

# to see choices related to our question number 1
Todo_appQuestionModel.query.get_or_404(1).choices

# to see all our choices
Todo_appChoiceModel.query.all()
dir(Todo_appChoiceModel.query) # to see many other method

for i in Todo_appChoiceModel.query.all():
  i.selector.question_text, i.choice_text


"""
