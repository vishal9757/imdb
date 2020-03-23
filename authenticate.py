"""
Script to authenticate and create users
"""
import os
import redis

REDIS_PORT = int(os.environ['REDIS_PORT'])
REDIS_HOST = os.environ['REDIS_HOST']
EXPIRY_TIME = 60

def get_redis_client(_db):
    """
    Function to get redis client
    """
    redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=_db)
    return redis_client

def authentic_user(user_name, password):
    """
    Function to authenticate super user
    """
    db_number = os.environ['REDIS_DB']
    redis_client = get_redis_client(db_number)
    if redis_client.get(user_name) and (redis_client.get(user_name).decode() == password):
        return True
    return False
