# from sakyum software, your app (todo_app) forms.py file
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class QuestionForm(FlaskForm):
  """ Todo_app default Question form """
  question_text = TextAreaField('Question_Text', validators=[DataRequired()])
  submit = SubmitField('create')


class ChoiceForm(FlaskForm):
  """ Todo_app default Choice form """
  question_id = StringField('Question_Id', validators=[DataRequired()])
  choice_text = StringField('Choice_Text', validators=[DataRequired(), Length(min=2, max=20)])
  submit = SubmitField('create')
