from flask import Flask
from flask_cors import CORS

from endpoints import listings

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['CORS_HEADERS'] = 'Content-Type'
    cors = CORS(app, resources={r"/listings": {"origins": ["localhost", "http://localhost:3000"]}})
    app.register_blueprint(listings, url_prefix='')
    return app
        
if __name__ == '__main__':
    app = create_app()
    app.app_context().push()
    app.run(port=8000, host="0.0.0.0")