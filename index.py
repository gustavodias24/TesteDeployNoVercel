from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"index": "Ok"})


@app.route("/post", methods=["POST"])
def postagem():
    return jsonify({"post": "Ok"})


@app.route("/google")
def google():
    return render_template("google.html")


if __name__ == "__main__":
    app.run()
