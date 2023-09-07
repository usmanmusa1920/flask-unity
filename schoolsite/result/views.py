# from flask_unity software, your app (result) views.py file
from flask import (render_template, Blueprint)
from flask_unity.utils import footer_style, template_dir, static_dir
from flask_unity.contrib import db
# from .models import <app_models>
# from .forms import <model_form>


result = Blueprint(
    'result', __name__, template_folder=template_dir(), static_folder=static_dir('result')
)


@result.route('/result/', methods=['GET', 'POST'])
def index():
    context = {
        'head_title': 'result',
        'footer_style': footer_style,
    }
    return render_template('result/index.html', context=context)
