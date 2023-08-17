:tocdepth: 2

HTML forms
##########

We can instead of using html file to write our forms, we can use this form feature that will represent our form template in the form of class and some methods.

To create forms we have to go into our app forms.py **exam/forms.py**. We will notice some default import::

    from flask_wtf import FlaskForm
    from wtforms import StringField, SubmitField, TextAreaField
    from wtforms.validators import DataRequired, Length

Now below we are to start defining our forms, I will first start with **QuestionForm** form which will look like::

    class QuestionForm(FlaskForm):
        """ Exam default Question form """
        question_text = TextAreaField('Question_Text', validators=[DataRequired()])
        submit = SubmitField('create')

Now I will define the **ChoiceForm** model which will look like::

    class ChoiceForm(FlaskForm):
        """ Exam default Choice form """
        question_id = StringField('Question_Id', validators=[DataRequired()])
        choice_text = StringField('Choice_Text', validators=[DataRequired(), Length(min=2, max=20)])
        submit = SubmitField('create')

Next is to go to our app views.py file **exam/views.py** and import the forms, make sure your follow the order of the import (you will see a prototype commented in your app views.py file above) which look like::

    from flask import (render_template, Blueprint)
    from flask_unity.utils import footer_style, template_dir, static_dir
    # from <project_name>.config import db
    # from .models import <app_models>
    # from .forms import <model_form>

Uncomment the fifth line, like::

    from flask import (render_template, Blueprint)
    from flask_unity.utils import footer_style, template_dir, static_dir
    # from <project_name>.config import db
    # from .models import <app_models>
    from .forms import QuestionForm, ChoiceForm
