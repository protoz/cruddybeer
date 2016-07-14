from flask import Flask, render_template

app = Flask(__name__)

def db_connect():
    db = "blah"
    return db

#Check if the brewery currently exists, if it does not, add brewery
def brewery_add():
    return "Add Brewery"

#Check if the brewery currently exists, if it does, remove brewery
def brewery_remove():
    return "Remove Brewery"

#Check if beer exists for any brewery. If not, add it to specified brewery
def beer_add():
    return "Add Beer"

#Check if beer exists in selected brewery, if it does, remove it
def beer_remove():
    return "Remove Beer"

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()