from flask import Flask
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config.from_object('cruddybeer.config')
db = MongoEngine(app)


def register_blueprints():
    # Prevents circular imports

    import cruddybeer.views
    app.register_blueprint(views.breweries)


register_blueprints()
