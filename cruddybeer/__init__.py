from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
db = MongoEngine(app)
app.config.from_object('cruddybeer.config')
#app.config.from_envvar('YOURAPPLICATION_SETTINGS')

import cruddybeer.config
import cruddybeer.models

def register_blueprints(app):
    # Prevents circular imports
    from cruddybeer.views import breweries
    app.register_blueprint(breweries)

register_blueprints(app)

if __name__ == "__main__":
    app.run()