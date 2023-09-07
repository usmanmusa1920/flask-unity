# from flask_unity software, your (schoolsite) project routes.py file
from flask import (render_template, Blueprint)
from flask_unity.utils import footer_style, template_dir, static_dir, reg_blueprints_func
from exam.views import exam
from result.views import result
from datetime import datetime
from exam.models import ExamQuestionModel, ExamChoiceModel


schoolsite = Blueprint(
    'schoolsite', __name__, template_folder=template_dir(), static_folder=static_dir('schoolsite')
)


reg_blueprints = reg_blueprints_func(
    schoolsite,
    exam,
    result,
)


@schoolsite.route('/', methods=['POST', 'GET'])
def index():
    questions = ExamQuestionModel.query.all()
    context = {
        'questions': questions,
        'project_name': 'schoolsite',
        'footer_style': footer_style,
        'the_year': datetime.today().year,
    }
    # return render_template('schoolsite/index.html', context=context)
    return render_template('schoolsite/questions.html', context=context)


@schoolsite.route('/question/choice/<int:q_id>/', methods=['POST', 'GET'])
def question(q_id):
    # choices = ExamChoiceModel.query.get_or_404(q_id)
    choices = ExamChoiceModel.query.all()
    context = {
        'choices': choices,
        'project_name': 'schoolsite',
        'footer_style': footer_style,
        'the_year': datetime.today().year,
    }
    # return render_template('schoolsite/index.html', context=context)
    return render_template('schoolsite/choice.html', context=context)
    
    
# overwrite (customise) error pages here
