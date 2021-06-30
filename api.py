from datetime import datetime

from flask import Flask, request, jsonify
from datastore import fetch_all_topics, fetch_topic_posts, store_topic, store_post

app = Flask(__name__)


@app.route('/')
def home():
    """Return all blog posts"""
    time = datetime.datetime.now()
    return jsonify({"message": "Hello World", "time": time})


@app.route("/topics", methods=['GET'])
def get_topics():
    topics = fetch_all_topics()
    response = jsonify(topics)
    response.status_code = 200
    return response


@app.route("/topics", methods=['POST'])
def add_topic():
    topic = request.get_json(force=True)
    id = topic['topic'].replace(' ', '-').lower()
    store_topic(id, **topic)
    response = jsonify({"message": "created"})
    response.status_code = 201
    return response


@app.route("/topics/<topic_id>/posts", methods=['GET'])
def get_posts(topic_id):
    posts = fetch_topic_posts(str(topic_id))
    response = jsonify(posts)
    response.status_code = 200
    return response


@app.route("/topics/<topic_id>/posts", methods=['POST'])
def add_post(topic_id):
    post = request.get_json(force=True)
    id = datetime.today().strftime('%Y-%m-%d') + "-" + \
        post["title"].replace(" ", "-").lower()
    store_post(str(topic_id), id, **post)
    response = jsonify({"message": "created"})
    response.status_code = 201
    return response


@app.errorhandler(404)
def bad_request():
    response = jsonify({"error": "not found"})
    response.status_code = 404
    return response


@app.errorhandler(401)
def unauthorized():
    response = jsonify({"error": "unauthorized"})
    response.status_code = 401
    return response


if __name__ == "__main__":
    # This is used when running the app locally only
    app.run(host='127.0.0.1', port=8080, debug=True)
