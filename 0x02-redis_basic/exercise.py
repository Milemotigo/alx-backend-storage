#!/usr/bin/env python3
'''
    Cache class. In the __init__ method, store an instance of the Redis client as a private
    variable named _redis (using redis.Redis()) and flush the instance using flushdb
'''

import redis
from uuid import uuid4
from typing import Union

class Cache:
    '''Represents an object for storing data in a Redis data storage.
    '''

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushall(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Create a store method that takes a data argument and returns a string
        '''
        key = str(uuid4())
        self._redis.set(key, data)
        return key