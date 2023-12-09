from flask import Flask
from flask_cors import CORS

from api.constants import api_prefix, origins

from api.endpoints import (
    listings, 
    contacts, 
    transactions,
    bar_graph,
    team,
    geography
)

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['CORS_HEADERS'] = 'Content-Type'
    cors = CORS(app, resources={r"/*": {"origins": origins}})
    app.register_blueprint(listings, url_prefix=api_prefix)
    app.register_blueprint(contacts, url_prefix=api_prefix)
    app.register_blueprint(transactions, url_prefix=api_prefix)
    app.register_blueprint(bar_graph, url_prefix=api_prefix)
    app.register_blueprint(team, url_prefix=api_prefix)
    app.register_blueprint(geography, url_prefix=api_prefix)

    return app
        
if __name__ == '__main__':
    app = create_app()
    app.app_context().push()
    app.run(port=8000, host="0.0.0.0")