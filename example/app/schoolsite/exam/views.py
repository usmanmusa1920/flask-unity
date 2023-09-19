# from flask_unity software, your app (exam) views.py file
from flask import (render_template, Blueprint, redirect, flash, request, url_for)
from flask_login import current_user, login_required
from flask_unity.utils import footer_style, template_dir, static_dir
from flask_unity.contrib import db
from flask_unity.auth.models import User
from .models import ExamQuestionModel, ExamChoiceModel
# from .forms import <model_form>
from datetime import datetime


exam = Blueprint(
    'exam', __name__, template_folder=template_dir(), static_folder=static_dir('exam')
)


@exam.route('/exam/', methods=['GET', 'POST'])
def default_index():
    context = {
        'head_title': 'exam',
        'footer_style': footer_style,
    }
    return render_template('exam/default_index.html', context=context)


@exam.route('/create/exam/question/', methods=['GET', 'POST'])
@login_required
def create_question():
    if request.method == 'POST':
        title = request.form['title']
        summary = request.form['summary']
        c_num_1 = request.form['c_num_1']
        c_num_2 = request.form['c_num_2']
        c_num_3 = request.form['c_num_3']
        c_num_4 = request.form['c_num_4']
        
        usr = User.query.filter_by(username=current_user.username).first()
        quest = ExamQuestionModel(title=title, summary=summary, user=usr)
        db.session.add(quest)
        db.session.commit()

        c1_1 = ExamChoiceModel(choice_text=c_num_1, question_id=quest.id)
        c1_2 = ExamChoiceModel(choice_text=c_num_2, question_id=quest.id)
        c1_3 = ExamChoiceModel(choice_text=c_num_3, question_id=quest.id)
        c1_4 = ExamChoiceModel(choice_text=c_num_4, question_id=quest.id)
        db.session.add(c1_1)
        db.session.add(c1_2)
        db.session.add(c1_3)
        db.session.add(c1_4)
        db.session.commit()
        flash('Your just create one question', 'succes')
        return redirect(url_for('exam.index'))
    return render_template('exam/create_question.html', the_year=datetime.today().year)

