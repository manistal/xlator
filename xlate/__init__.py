
from flask import Flask
import os

def create_app(config=None):
    """
    XLate Application Factory
        Constructs Flask WSGI Application and applies ENV Vars for Bluemix API to Config Object
        Attaches view blueprints from the view module to render the translator 
    return -- Flask Application 
    """
    app = Flask(__name__, template_folder='static/html', static_folder='static')
    app.config['BLUEMIX_API_KEY'] = os.environ.get('BLUEMIX_API_KEY')
    app.config['BLUEMIX_API_URL'] = os.environ.get('BLUEMIX_API_URL')

    from .views import translator 
    app.register_blueprint(translator.bp)
    return app

