import flask

from infrastructure.view_modifiers import response
from services import package_service, user_service

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
@response(template_file='home/index.html')
# those are called view-methods
def index(template='home/index.html'):
    return {
        'releases': (package_service.get_latest_releases()),
        'package_count': package_service.get_package_count(),
        'release_count': package_service.get_release_count(),
        'user_count': user_service.get_user_count(),
    }
    # return flask.render_template(template, **data)


@blueprint.route('/about')
@response(template_file='home/about.html')
def about():
    return {}
