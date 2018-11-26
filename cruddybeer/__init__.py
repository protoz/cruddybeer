from flask import Flask
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config.from_object('cruddybeer.config')
db = MongoEngine(app)


def register_blueprints():
    # Prevents circular imports

    import cruddybeer.config
    import cruddybeer.models
    from cruddybeer.views import breweries
    app.register_blueprint(breweries)


register_blueprints()

if __name__ == "__main__":
    app.run()
