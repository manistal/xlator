
from flask import Blueprint, render_template, request

bp = Blueprint('translator', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/translate_textbox', methods=['POST'])
def translate_textbox():
    print(request.form)
    return render_template('index.html')

@bp.route('/translate_file', methods=['POST'])
def translate_file():
    print(request.form)
    return render_template('index.html')
