from flask import Flask
from flask_mongoengine import MongoEngine
import cruddybeer.config
import cruddybeer.models

app = Flask(__name__)
db = MongoEngine(app)
app.config.from_object('cruddybeer.config')
# cruddybeer.config.from_envvar('YOURAPPLICATION_SETTINGS')


def register_blueprints(app):
    # Prevents circular imports
    from cruddybeer.views import breweries
    app.register_blueprint(breweries)

register_blueprints(app)

if __name__ == "__main__":
    app.run()
