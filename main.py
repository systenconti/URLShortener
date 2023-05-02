from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def shortener():
    if request.method == "POST":
        url_received = request.form["long_url"]
        print(url_received)
        return url_received
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
