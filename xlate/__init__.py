
from flask import Flask

def create_app(config=None):
    app = Flask(__name__, template_folder='static/html', static_folder='static')

    from .views import translator 
    app.register_blueprint(translator.bp)

    return app

