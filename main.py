import datetime

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def root():
    """Return all blog posts"""
    datetime.datetime(2018, 1, 1, 10, 0, 0)
    return render_template('index.html', time=datetime.datetime.now())


if __name__ == "__main__":
    # This is used when running the app locally only
    app.run(host='127.0.0.1', port=8080, debug=True)