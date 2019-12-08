
from flask import Blueprint, render_template, request, redirect, url_for

from . import bluemix_translate_api as bta

bp = Blueprint('translator', __name__)

@bp.route('/')
def index():
    original_text = request.args.get('original_text', '')
    result_text = request.args.get('result_text', '')
    return render_template('index.html', 
        original_text=original_text, 
        result_text=result_text)

@bp.route('/translate_textbox', methods=['POST'])
def translate_textbox():
    original_text = request.form.get('translation_text')
    result_text = bta.identify_and_translate(original_text)
    return redirect(url_for('.index', original_text=original_text, result_text=result_text))

