
import pandas as pd
from flask import Blueprint, render_template, request, redirect, url_for, current_app

from .bluemix_translate_api import BluemixLanguageTranslator

bp = Blueprint('translator', __name__)

def get_language_selections():
    blt = BluemixLanguageTranslator(current_app.config['BLUEMIX_API_URL'], current_app.config['BLUEMIX_API_KEY'])
    # Get map of language codes to language names #
    # THIS SHOULDNT BE SEPERATE IBM!! # 
    languages = blt.get_identifiable_languages()
    lang_df = pd.DataFrame(languages).set_index('language')
    def get_language_name(model_id):
        try:
            return lang_df.loc[model_id, 'name']
        except KeyError as e:
            return model_id

    # Add in display names for language codes 
    language_models = blt.get_available_language_models()
    language_models = [ { **model, 
        'source_name': get_language_name(model['source']),
        'target_name': get_language_name(model['target'])
    } for model in language_models ]
    return language_models

@bp.route('/')
def index():
    original_text = request.args.get('original_text', '')
    result_text = request.args.get('result_text', '')
    return render_template('index.html', 
        original_text=original_text, 
        result_text=result_text,
        language_selections=get_language_selections())

@bp.route('/translate_textbox', methods=['POST'])
def translate_textbox():
    blt = BluemixLanguageTranslator(current_app.config['BLUEMIX_API_URL'], current_app.config['BLUEMIX_API_KEY'])
    original_text = request.form.get('translation_text')
    language_model = request.form.get('language_model', 'detect')
    if 'detect' in language_model.lower():
        source_language = blt.identify_language(original_text)
        language_model = f"{source_language}-en"
    result_text = blt.translate_text(original_text, model_id=language_model)
    return redirect(url_for('.index', original_text=original_text, result_text=result_text))
