
from flask import Blueprint, render_template, request

bp = Blueprint('translator', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/translate_textbox', methods=['POST'])
def translate_textbox():
    print(request.form)
    result = request.form.get('translation_text')
    return render_template('result.html', result=result)

@bp.route('/translate_file', methods=['POST'])
def translate_file():
    print(request.form)
    result = request.form.get('translation_file')
    return render_template('index.html', result=result)
