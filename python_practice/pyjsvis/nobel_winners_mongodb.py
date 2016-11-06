#!/usr/bin/env python
"""
__author__ = ShannonB., 10/2/16
"""

import sys
from os import path
import json
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

    with open(path.join(path.dirname(sys.argv[0]), 'nobel_winners', 'nobel_winners.json')) as f:
        nobel_winners = json.load(f)
        f.close()

    print nobel_winners

    # db = get_mongo_database(DB_NOBEL_PRIZE)
    # coll = db[COLL_WINNERS]
    #
    # coll.insert(nobel_winners)

if __name__ == '__main__':
    main()
