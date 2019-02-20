from flask import Flask, render_template,session

from flask_session import Session

from tempfile import mkdtemp

app = Flask(__name__)

app.config["SESSSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

board = []

@app.route("/")
def index():

	if "board" not in session:

		session["board"] = [ [ None, None, None],

		[ None, None, None],

		[ None, None, None]

		]

		session["turn"] = "x"

	return render_template("game.html", game = session["board"], turn = session["turn"])



@app.route("/play/<int:row>/<int:col>")
def play(row,col):

	return "played a move"














