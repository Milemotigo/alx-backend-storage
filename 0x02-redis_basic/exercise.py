#!/usr/bin/env python3
'''
    Cache class. In the __init__ method, store an instance of the Redis client as a private
    variable named _redis (using redis.Redis()) and flush the instance using flushdb
'''

import redis
from uuid import uuid4
from typing import Union

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushall()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Create a store method that takes a data argument and returns a string
        '''
        key = str(uuid4())

        if data is type(str, bytes):
            self._redis.set(key, data)
        if data is type(int, float):
            self._redis.set(key, str(data))
        return key