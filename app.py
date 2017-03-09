from flask import Flask, render_template, request

app = Flask("diagnos")

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/contact/", methods=["GET", "POST"])
def contact():
	if request.method == "POST":
		return "Tack!"
	return render_template("contact.html")

if __name__ == "__main__":
	app.run("0.0.0.0", debug=True)