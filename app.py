from flask import Flask, render_template, request
from models import *	

app = Flask("tibialoot")

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/contact/")
def spawn_statistics():
	return render_template("contact.html")

if __name__ == "__main__":
	app.run("0.0.0.0", debug=True)