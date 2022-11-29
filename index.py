from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"index": "Ok"})

@app.route("/post", methods=["POST"])
def postagem():
    return jsonify({"post": "Ok"})


if __name__ == "__main__":
    app.run()
