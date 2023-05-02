from flask import Flask, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from credentials import secret_key
import os
import string
import random


app = Flask(__name__)
app.config["SECRET_KEY"] = secret_key
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://postgres:{os.environ.get('DATABASE_PASS')}@localhost:5432/urlshortener"

db = SQLAlchemy(app)


class Urls(db.Model):
    url_id = db.Column("url_id", db.Integer, primary_key=True)
    long = db.Column("long", db.String())
    short = db.Column("short", db.String(4))

    def __init__(self, long, short):
        self.long = long
        self.short = short


def shorten_url():
    letters = string.ascii_letters
    while True:
        rand_letters = random.choices(letters, k=4)
        rand_letters = "".join(rand_letters)
        short_url = Urls.query.filter_by(short=rand_letters).first()
        if not short_url:
            return rand_letters


@app.route("/", methods=["POST", "GET"])
def shortener():
    if request.method == "POST":
        url_received = request.form["long_url"]
        found_url = Urls.query.filter_by(long=url_received).first()
        if found_url:
            flash(f"http://127.0.0.1:5000/{found_url.short}", "success")
            return redirect(url_for("shortener"))
        else:
            short_url = shorten_url()
            new_url = Urls(url_received, short_url)
            db.session.add(new_url)
            db.session.commit()
            flash(f"http://127.0.0.1:5000/{short_url}", "success")
            return redirect(url_for("shortener"))

    else:
        return render_template("shortener.html")
    
@app.route('/<short_url>')
def redirection(short_url):
    long_url = Urls.query.filter_by(short=short_url).first()
    if long_url:
        return redirect(long_url.long)
    else:
        return "<h1>Url doesn't exist</h1>"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
