# from sakyum software, your app (todo_app) models.py file
from datetime import datetime
from todo_project.config import db

"""
when ever you create a model, make sure you import it in your
project config.py file before you run your application to avoid error
"""

class Question(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  question_text = db.Column(db.Text, nullable=False)
  choices = db.relationship('Choice', backref='selector', lazy=True)

  def __repr__(self):
    return f"Question number ('{self.id}', posted on: '{self.date_posted}')"
    
  # the `Choice` is the choice model class below
  # the `selector` is the attribute that we can use to get selector who choose the choice
  # the `lazy` argument just define when sqlalchemy loads the data from the database

class Choice(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
  # you can pass a keyword argument of `unique=True` in the below choice_text field
  # that will make it unique across the entire table of choice
  choice_text = db.Column(db.String(100), nullable=False)

  def __repr__(self):
    return f"Choice of ('{self.question_id}', '{self.date_posted}')"


"""
# :move on to terminal and paste the following command,
# :( in python interpreter ) make sure you are within that your virtual environment


from todo_project.config import db
from todo_app.models import Question, Choice


# :method to create the tables and database, if it doesn't create db file,
run the below command. But if it create just ignore
db.create_all()


q1 = Question(question_text="Is sakyum an extension of flask web framework?")
q2 = Question(question_text="Is flask better with sakyum")

db.session.add(q1)
db.session.add(q2)
db.session.commit()

the_q1 = Question.query.get_or_404(1)
the_q2 = Question.query.get_or_404(2)

c1_1 = Choice(choice_text="Yes, it is", question_id=the_q1.id)
c1_2 = Choice(choice_text="No, it is not", question_id=the_q1.id)
c1_3 = Choice(choice_text="I don't no", question_id=the_q1.id)

c2_1 = Choice(choice_text="Yes for sure", question_id=the_q2.id)
c2_2 = Choice(choice_text="Always the best", question_id=the_q2.id)
c2_3 = Choice(choice_text="All the time", question_id=the_q2.id)

db.session.add(c1_1)
db.session.add(c1_2)
db.session.add(c1_3)

db.session.add(c2_1)
db.session.add(c2_2)
db.session.add(c2_3)

db.session.commit()

# to see all our questions
Question.query.all()
dir(Question.query) # to see many other method

# to see choices related to our question number 1
Question.query.get_or_404(1).choices

# to see all our choices
Choice.query.all()
dir(Choice.query) # to see many other method

for i in Choice.query.all():
  i.selector.question_text, i.choice_text

"""
