#!/usr/bin/env python3
'''searched by topic
'''

def schools_by_topic(mongo_collection, topic):
    '''
        Prototype: def schools_by_topic(mongo_collection, topic):
        mongo_collection will be the pymongo collection object
        topic (string) will be topic searched
    '''

    lst = list(mongo_collection.find({"topics": topic}))
    return lst