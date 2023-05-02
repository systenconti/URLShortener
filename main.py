from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from credentials import secret_key
import os


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


@app.route("/", methods=["POST", "GET"])
def shortener():
    if request.method == "POST":
        url_received = request.form["long_url"]
        print(url_received)
        return url_received
    else:
        return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
