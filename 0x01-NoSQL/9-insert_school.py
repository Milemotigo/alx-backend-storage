#!/usr/bin/env python3
'''def insert_school(mongo_collection, **kwargs):
'''

def insert_school(mongo_collection, **kwargs):
    """ Python function that inserts a new document in a collection based on kwargs
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id