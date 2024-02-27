#!/usr/bin/env python3
"""task 8"""


def list_all(mongo_collection):
    """Lists all documents in a collection."""
    return [doc for doc in mongo_collection.find()]
