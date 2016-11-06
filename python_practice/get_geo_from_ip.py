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

VERSION = '0.2.0'
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

    parser.add_argument('-l', '--list', dest='ip_list', action='store',
                        help="path to list containing single column of IP addresses that you want to geocode.")

    parser.add_argument('-o', '--output_to', dest='output_path', action='store',
                        help="path to some output dir/filename.txt you want to write results to.")

    return parser


def main():

    parser = get_parser()
    args = parser.parse_args()

    if args.ip_list:

        list_file_path = path.join(args.ip_list)

        try:
            with open(list_file_path, 'r') as f:
                ip_list_file_contents = f.read()

        except Exception, e:
            print('something wrong?', e)

        finally:

            # TODO: swap this out later
            print(ip_list_file_contents)

    else:

        send_url = 'http://freegeoip.net/json'
        r = requests.get(send_url)
        j = json.loads(r.text)
        lat = j['latitude']
        lon = j['longitude']

        print('\nYour Current Location (Lat, Lon): {}'.format((lat, lon)))


if __name__ == '__main__':
    main()
