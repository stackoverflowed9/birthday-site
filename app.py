from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/message")
def message():
    return render_template("message.html")


@app.route("/collage")
def collage():
    return render_template("collage.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render gives a port
    app.run(host="0.0.0.0", port=port)        # Bind to 0.0.0.0
