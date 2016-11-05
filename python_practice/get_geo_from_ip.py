#!/usr/bin/env python
"""
__author__ = 
__created__ = 11/5/16
"""

import os
import sys
from os import path
import argparse
import requests
import json

VERSION = '0.1.0'
LAST_MOD = '11/5/16'

# Customize
program_desc = 'v{}, last-modified {}: \n \
Single sentence describing module purpose.'.format(VERSION, LAST_MOD)


# May or may not need a parser, but just in case... 
def get_parser():
    """
    generic parser uses above info
    """
    parser = argparse.ArgumentParser(description=program_desc)

    # Customize
    parser.add_argument('-o1', '--option1', dest='option1_arg', action='store',
                        help="does what option1 is supposed to do")

    return parser


def main():

    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    lat = j['latitude']
    lon = j['longitude']

    print('\nYour Current Location (Lat, Lon): {}'.format((lat, lon)))

    parser = get_parser()
    args = parser.parse_args()

    # Customize (refactor opt1 -> blah)
    if args.option1_arg:
        # Customize
        what_option_one_does = args.option1_arg1
        print('\nOption Selected: {}'.format(what_option_one_does))


if __name__ == '__main__':
    main()
