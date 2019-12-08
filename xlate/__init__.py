
from flask import Flask

def create_app(config=None):
    app = Flask(__name__, template_folder='static/html', static_folder='static')
    app.config.from_pyfile('config/default.py')

    from .views import translator 
    app.register_blueprint(translator.bp)
    return app

