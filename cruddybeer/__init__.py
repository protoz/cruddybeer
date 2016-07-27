from flask import Flask
from flask_mongoengine import MongoEngine
#flask_mongoengine 0.7.5 still complains about flask.ext.mongoengine being deprecated.  Fixed in unreleased 0.8.0

app = Flask(__name__)
db = MongoEngine(app)
app.config.from_object('cruddybeer.config')
#cruddybeer.config.from_envvar('YOURAPPLICATION_SETTINGS')

import cruddybeer.config
import cruddybeer.models

def register_blueprints(app):
    # Prevents circular imports
    from cruddybeer.views import breweries
    app.register_blueprint(breweries)

register_blueprints(app)

if __name__ == "__main__":
    app.run()