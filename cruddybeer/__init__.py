from flask import Flask
app = Flask(__name__)
app.config.from_object('cruddybeer.config')
#app.config.from_envvar('YOURAPPLICATION_SETTINGS')

import cruddybeer.views
import cruddybeer.config
import cruddybeer.models

if __name__ == "__main__":
    app.run()