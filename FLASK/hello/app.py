# app.py
# Minimal Flask application with a home page and a greeting route.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet")
def greet():
    name = request.args.get("name", "world")
    return render_template("greet.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
