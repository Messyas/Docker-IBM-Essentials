from flask import Flask # type: ignore

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Beautiful World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
