from flask import Blueprint, render_template

my_blueprint = Blueprint('my_bluprint', __name__, url_prefix="/blueprint")

@my_blueprint.route('/hello')
def hello():
    return "<h1> Hello from the Blueprint! <h1>"