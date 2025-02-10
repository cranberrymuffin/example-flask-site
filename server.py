from datetime import datetime

from flask import Flask, render_template, request
from imgconverter import img2ascii
app = Flask(__name__)


@app.route("/")
def hello_world():
    print("new web request")
    return f"hello from disco!!! the datetime is {datetime.now()}"

@app.route("/cranberrymuffin")
def ascii_test():
    if request.method == 'GET':
        return render_template('hello_world.html', variable_name=img2ascii.image_to_ascii())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
