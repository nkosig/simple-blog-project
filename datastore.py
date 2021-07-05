# https://github.com/GoogleCloudPlatform/python-docs-samples/blob/9869d47937b45840072485f86248438efa1c955d/datastore/cloud-client/snippets.py

from datetime import datetime
from google.cloud import datastore

client = datastore.Client()


def store_topic(id, **topic):

    with client.transaction():
        key = client.key("Topic", id)
        entity = datastore.Entity(key=key)

        entity["created_at"] = datetime.utcnow()
        entity["id"] = id

        entity.update(topic)
        client.put(entity)


def fetch_all_topics():
    query = client.query(kind="Topic")

    return list(query.fetch())


def store_post(topic_id, post_id, **post):

    parent_key = client.key("Topic", topic_id)
    key = client.key("Post", post_id, parent=parent_key)
    entity = datastore.Entity(key=key)

    entity["created_at"] = datetime.utcnow()
    entity["id"] = post_id

    entity.update(post)
    client.put(entity)


def fetch_topic_posts(topic_id):

    ancestor_key = client.key("Topic", topic_id)
    query = client.query(kind="Post", ancestor=ancestor_key)

    return list(query.fetch())


def fetch_all_posts(limit, cursor=None):

    query = client.query(kind="Post")
    query.order = ["-created_at"]
    query_iter = query.fetch(start_cursor=cursor, limit=limit)
    page = next(query_iter.pages)
    next_cursor = query_iter.next_page_token

    return list(page), str(next_cursor)
