import flask

app = flask.Flask('mega')

@app.route('/')
def hello_world():
    return 'Hello World.'

app.run()
