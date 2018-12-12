import os
import sys
from flask_script import Manager, Server
from cruddybeer import create_app

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

manager = Manager(create_app)

# Turn on debugger by default and reloader
manager.add_command(
    "runserver", Server(use_debugger=True, use_reloader=True, host="0.0.0.0")
)

if __name__ == "__main__":
    manager.run()
