from flask import Flask, request
from markupsafe import escape
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/about")
def about():
    #return "<p>This is the instructions manual</p>"
    return render_template('about.html')


@app.route("/player/<id>")
def player(id):
    return render_template('player.html', id=id)
    #return f'Player {escape(id)}'

@app.get("/player_api/<int:id>")
def player_get(id):
    data = ['Pepe', 'Carlos', 'Manuel','Victoria']
    try:
        return {
            "user_id": id,
            "name": data[id]
        }
    except:
        return 'Not found', 404
