from flask import Flask
from .views import my_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(my_blueprint)
    return app
