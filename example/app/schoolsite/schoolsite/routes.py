# from flask_unity software, your (schoolsite) project routes.py file
from flask import render_template
from flask_unity.utils import reg_blueprints_func
from exam.views import exam
from exam.models import ExamQuestionModel, ExamChoiceModel
from custom_auth.views import custom_auth
from datetime import datetime


reg_blueprints = reg_blueprints_func(
    exam,
    custom_auth,
)


@exam.route('/', methods=['POST', 'GET'])
def index():
    questions = ExamQuestionModel.query.all()
    return render_template('exam/index.html', questions=questions, the_year=datetime.today().year)


@exam.route('/question/choice/<int:q_id>/', methods=['POST', 'GET'])
def question(q_id):
    # choices = ExamChoiceModel.query.get_or_404(q_id)
    choices = ExamChoiceModel.query.all()
    return render_template('exam/choice.html', choices=choices, the_year=datetime.today().year)


# overwrite (customise) error pages here
