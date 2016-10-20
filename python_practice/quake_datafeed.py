#!/usr/bin/env python
"""
__author__ = , 10/8/16
"""

import os
import sys
from os import path
import json
import urllib2
import datetime
import argparse


def get_parser():

    parser = argparse.ArgumentParser()

    parser.add_argument('-m', '--magnitude', action="store")

    parser.add_argument('-t', '--timeframe', action="store", choices=['hour', 'week', 'day', 'month'])

    return parser


def print_results(data):

    json_data = json.loads(data)

    if 'title' in json_data['metadata']:
        print json_data['metadata']['title']

    count = json_data['metadata']['count']
    print str(count) + ' events found'

    for i in json_data['features']:

        if i['properties']['mag'] >= 4.0:
            print '%2.1f' % i['properties']['mag'], i['properties']['place']


def main():

    parser = get_parser()

    args = parser.parse_args()

    if args.timeframe:

        t = args.timeframe
        print 'Finding Events within the last {}'.format(t)
    else:
        t = 'week'

    if args.magnitude:
        mag = args.magnitude
        print '\nMag requested: {}'.format(mag)

        if mag < 2.5:
            mag = 1  # less than 2.5 gets them the 1.0+ range
        elif 2.5 <= mag < 4.5:
            mag = 2.5
        else:
            mag = 4.5
    else:
        mag = 2.5

    # time_elapsed = datetime.datetime.now() - datetime.timedelta(weeks=1)
    #
    # print '{}'.format(datetime.time.strftime(datetime.time(time_elapsed)))

    api_url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/{}_{}.geojson'.format(mag, t)

    page = urllib2.urlopen(api_url)

    data = page.read()

    if data:
        print_results(data)

if __name__ == '__main__':
    main()
