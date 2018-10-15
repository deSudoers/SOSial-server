from flask import Flask, jsonify, render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/test", methods=["GET", "POST"])
def test():
    response = {"response": "success"}
    if request.method == "POST":
        json_data = request.get_json()
        response["message"] = json_data["message"]
    return jsonify(response), 201


if __name__ == '__main__':
    app.run()
