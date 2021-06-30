# https://github.com/GoogleCloudPlatform/python-docs-samples/blob/9869d47937b45840072485f86248438efa1c955d/datastore/cloud-client/snippets.py

from datetime import datetime
from google.cloud import datastore

client = datastore.Client()


def store_topic(id, **topic):

    with client.transaction():
        key = client.key("Topic", id)
        entity = datastore.Entity(key=key)

        topic["created_at"] = datetime.utcnow()

        entity.update(topic)
        client.put(entity)


def fetch_all_topics():
    query = client.query(kind="Topic")

    return list(query.fetch())


def store_post(topic_id, post_id, **post):

    topic_key = client.key("Topic", topic_id)
    post_key = client.key("Post", post_id, parent=topic_key)
    post_entity = datastore.Entity(key=post_key)

    post["created_at"] = datetime.utcnow()

    post_entity.update(post)

    client.put(post_entity)


def fetch_topic_posts(topic_id):

    topic_key = client.key("Topic", topic_id)
    query = client.query(kind="Post", ancestor=topic_key)

    return list(query.fetch())
