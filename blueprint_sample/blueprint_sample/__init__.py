from flask import Flask

def create_app():

    app = Flask(__name__)

    @app.route('/')
    def index():
        return ('<h1>landing page</h1>')
    @app.route('/v1/users')
    def v1_users():
        return 'v1'

    @app.route('/v2/users')
    def v2_users():
        return 'v2'

    return app