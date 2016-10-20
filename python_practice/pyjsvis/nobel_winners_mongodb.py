#!/usr/bin/env python
"""
__author__ = ShannonB., 10/2/16
"""

import os
import sys
from os import path
from pymongo import MongoClient

VERSION = '0.1.0'

client = MongoClient()

DB_NOBEL_PRIZE = 'nobel_prize'
COLL_WINNERS = 'winners'

db = client[DB_NOBEL_PRIZE]
coll = db[COLL_WINNERS]


def get_mongo_database(db_name, host='localhost', port=27017, username=None, password=None):

    #
    if username and password:
        mongo_url = 'mongodb://{}:{}@{}/{}'.format(username, password, host, db_name)
        conn = MongoClient(mongo_url)
    else:
        conn = MongoClient(host, port)

    return conn[db_name]


def main():
    pass

if __name__ == '__main__':
    main()
