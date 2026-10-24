import os

from flask import Flask, redirect, render_template, request, url_for

from database import add_entry, get_entries, init_db

app = Flask(__name__)
app.config["DATABASE"] = os.path.join(app.root_path, "guestbook.db")

MAX_NAME = 50
MAX_MESSAGE = 300

init_db(app.config["DATABASE"])


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name", "").strip()
    message = request.form.get("message", "").strip()

    error = None
    if not name or not message:
        error = "Naam aur paigham dono likhna zaroori hain."
    elif len(name) > MAX_NAME:
        error = f"Naam {MAX_NAME} harf se chota hona chahiye."
    elif len(message) > MAX_MESSAGE:
        error = f"Paigham {MAX_MESSAGE} harf se chota hona chahiye."

    if error:
        return render_template("form.html", error=error, name=name, message=message), 400

    add_entry(app.config["DATABASE"], name, message)
    return redirect(url_for("guestbook"))


@app.route("/guestbook")
def guestbook():
    entries = get_entries(app.config["DATABASE"])
    return render_template("guestbook.html", entries=entries)


if __name__ == "__main__":
    app.run(debug=True)
