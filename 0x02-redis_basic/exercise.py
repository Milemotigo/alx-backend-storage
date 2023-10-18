#!/usr/bin/env python3
'''
    Cache class. In the __init__ method, store an instance of the Redis client as a private
    variable named _redis (using redis.Redis()) and flush the instance using flushdb
'''
from functools import wraps
import redis
from uuid import uuid4
from typing import Union, Callable, Any

def count_calls(method: Callable) -> Callable:
    '''Tracks the number of calls made to a method in a Cache class.
    '''
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        '''returns the given method after incrementing its call counter.
        '''

        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper

class Cache:
    '''Represents an object for storing data in a Redis data storage.
    '''

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Store method that takes a data argument and returns a string
        '''
        key = str(uuid4())
        self._redis.set(key, data)
        return key
    
    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        '''This callable will be used to convert the data back to the desired format
        '''
        data = self._redis.get(key)
        if fn is not None:
            return fn(data)
        else:
            return data
        
    def get_str(self, key: str) -> str:
        '''Returns a string'''
        return self.get(key, fn=str)
    
    def get_int(self, key: int) -> int:
        '''Returns an integer'''
        return self.get(key, fn=int)