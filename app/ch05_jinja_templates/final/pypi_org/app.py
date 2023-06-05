import flask

app = flask.Flask(__name__)


def register_blueprint():
    from views import home_views
    app.register_blueprint(home_views.blueprint)
    from views import package_views
    app.register_blueprint(package_views.blueprint)
    from views import cms_views
    app.register_blueprint(cms_views.blueprint)

def main():
    register_blueprint()
    app.run(debug=True)


if __name__ == '__main__':
    main()
