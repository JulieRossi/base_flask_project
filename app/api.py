from datetime import datetime

from flask import Flask, render_template, jsonify

app = application = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/now')
def get_ts():
    return jsonify(datetime.now())


if __name__ == '__main__':
    app.run(debug=True)
