import flask

blueprint = flask.Blueprint('packages', __name__, template_folder='templates')


@blueprint.route('/project/<package_name>')
def package_details(package_name: str):
    return f"Package details for {package_name}"

# Only match the value if it is an integer
@blueprint.route('/<int:rank>')
def popular(rank: int):
    return f"The details for the {rank}th most popular package"
