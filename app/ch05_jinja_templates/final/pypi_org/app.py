import flask

app = flask.Flask(__name__)


def get_latest_packages():
    return [
        {'name': 'flask', 'version': '1.2.3'},
        {'name': 'sqlalchemy', 'version': '2.2.0'},
        {'name': 'passlib', 'version': '3.0.0'}
    ]


@app.route('/')
# those are called view-methods
def index(template='home/index.html'):
    test_packages = get_latest_packages()
    data = {'packages': test_packages}
    return flask.render_template(template, **data)


@app.route('/about')
def about():
    return flask.render_template('home/about.html')


if __name__ == '__main__':
    app.run(debug=True)
