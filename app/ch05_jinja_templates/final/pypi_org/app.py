import os.path

import flask
import data.db_session as db_session

app = flask.Flask(__name__)


def register_blueprint():
    from views import home_views
    app.register_blueprint(home_views.blueprint)
    from views import package_views
    app.register_blueprint(package_views.blueprint)
    from views import cms_views
    app.register_blueprint(cms_views.blueprint)


def setup_db():
    db_file = os.path.join(
        os.path.dirname(__file__),
        'db',
        'pypi.sqlite'
    )
    db_session.global_init(db_file)


def main():
    register_blueprint()
    setup_db()
    app.run(debug=True)


if __name__ == '__main__':
    main()
