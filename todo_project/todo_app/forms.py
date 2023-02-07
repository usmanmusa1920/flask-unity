# from sakyum software, your app (todo_app) forms.py file
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class TodoListForm(FlaskForm):
  name = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
  content = TextAreaField('Content', validators=[DataRequired()])
  submit = SubmitField('create todo')
