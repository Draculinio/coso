from flask import Flask, request
from markupsafe import escape
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()
app = Flask(__name__)
#db_name = 'coso_base'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coso_base' #+ db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

class User(db.Model):
    user_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    #email: Mapped[str] = mapped_column(String)

with app.app_context():
    db.create_all()

@app.route("/users/create/<name>", methods=["GET", "POST"])
def user_create(name):
    if request.method == "POST":
        user = User(
            name=name,
        )
        db.session.add(user)
        db.session.commit()
        return 'Created', 201

    #return render_template("user/create.html")
    return "Done"


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

@app.get("/players")
def players():
    #try:
    #    db.session.query(text('1')).from_statement(text('SELECT 1')).all()
    #    return '<h1>It works.</h1>'
    #except Exception as e:
    #    # e holds description of the error
    #    error_text = "<p>The error:<br>" + str(e) + "</p>"
    #    hed = '<h1>Something is broken.</h1>'
    #    return hed + error_text
    users = db.session.execute(db.select(User).order_by(User.user_id)).scalars()
    return users
