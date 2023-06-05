import flask

from infrastructure.view_modifiers import response
from services import package_services

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
@response(template_file='home/index.html')
# those are called view-methods
def index(template='home/index.html'):
    test_packages = package_services.get_latest_packages()
    return {'packages': test_packages}
    # return flask.render_template(template, **data)


@blueprint.route('/about')
@response(template_file='home/about.html')
def about():
    return {}
