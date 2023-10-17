#!/usr/bin/env python3
''' list all collections
'''

def list_all(mongo_collection):
    '''for doc in mongo_collection:
       if doc is none
       return []
       return[docs]
    '''

    return[doc for doc in mongo_collection.find()]