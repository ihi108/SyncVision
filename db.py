import redis
import os

cache = redis.from_url(os.environ.get("REDIS_URL"))

# For local development
# cache = redis.Redis()


def store_user_in_room(room_id, user_id):
    cache.sadd(room_id, user_id)


def remove_user_from_room(room_id, user_id):
    cache.srem(room_id, user_id)


def get_users_in_room(room_id):
    return cache.scard(room_id)


def remove_room_expiration(room):
    cache.persist(room)
