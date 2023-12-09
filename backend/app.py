from flask import Flask
from flask_cors import CORS

from api.endpoints import (
    listings, 
    contacts, 
    transactions,
    bar_graph
)

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['CORS_HEADERS'] = 'Content-Type'
    cors = CORS(app, resources={r"/*": {"origins": ["localhost", "http://localhost:3000"]}})
    app.register_blueprint(listings, url_prefix='/api/v1')
    app.register_blueprint(contacts, url_prefix='/api/v1')
    app.register_blueprint(transactions, url_prefix='/api/v1')
    app.register_blueprint(bar_graph, url_prefix='/api/v1')

    return app
        
if __name__ == '__main__':
    app = create_app()
    app.app_context().push()
    app.run(port=8000, host="0.0.0.0")