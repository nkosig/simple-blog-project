from datetime import datetime

from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import datastore

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    """Return all blog posts"""
    time = datetime.now()
    return jsonify({"message": "Hello World from Simple Blog App", "time": time})


@app.route("/topics", methods=['GET'])
def get_topics():
    topics = datastore.fetch_all_topics()
    response = jsonify(topics)
    response.status_code = 200
    return response


@app.route("/topics", methods=['POST'])
def add_topic():
    topic = request.get_json(force=True)
    id = topic['topic'].replace(' ', '-').lower()
    datastore.store_topic(id, **topic)
    data = jsonify({"message": "created"})
    response = Response(response=data, status=201)
    return response


@app.route("/posts", methods=['GET'])
def get_all_posts():
    posts, cursor = datastore.fetch_all_posts(limit=5)
    response = jsonify(posts=posts, next=cursor)
    response.status_code = 200
    return response


@app.route("/topics/<topic_id>/posts", methods=['GET'])
def get_posts(topic_id):
    posts = datastore.fetch_topic_posts(str(topic_id))
    response = jsonify(posts)
    response.status_code = 200
    return response


@app.route("/topics/<topic_id>/posts/<post_id>", methods=['GET'])
def get_post(topic_id, post_id):
    post = datastore.fetch_post(str(topic_id), str(post_id))
    response = jsonify(post)
    response.status_code = 200
    return response


@app.route("/topics/<topic_id>/posts", methods=['POST'])
def add_post(topic_id):
    post = request.get_json(force=True)
    id = datetime.today().strftime('%Y-%m-%d') + "-" + \
        post["title"].replace(" ", "-").lower()
    datastore.store_post(str(topic_id), id, **post)
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
    app.run(host='127.0.0.1', port=8084, debug=True)
