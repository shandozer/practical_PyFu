#!/usr/bin/env python
"""
__author__ = , 9/13/16
"""

import os
import sys
from os import path
from bs4 import BeautifulSoup
import urllib2
import codecs

BASE_URL = 'http://en.wikipedia.org/'
ANOTHER_URL = 'http://www.leafly.com/finder'

HEADERS = {'Users-Agent': 'Mozilla/5.0'}


def get_soup(base_url=BASE_URL, extension_url=''):

    info = urllib2.urlopen(base_url + extension_url)

    return BeautifulSoup(info)


def extract_tables_from_soup(soup):

    # tables = soup.select('table.sortable.wikitable')

    table = soup.select_one('table.sortable.wikitable')

    return table


def get_column_titles(table):

    cols = []

    for th in table.select_one('tr').select('th')[1:]:
        link = th.select_one('a')
        if link:
            cols.append({'name': link.text, 'href': link.attrs['href']})
        else:
            cols.append({'name': th.text, 'href': None})

    return cols


def get_winners(table):

    cols = get_column_titles(table)

    winners = []

    for row in table.select('tr')[1:-1]:

        year = int(row.select_one('td').text)

        for i, td in enumerate(row.select('td')[1:]):

            for winner in td.select('a'):

                href = winner.attrs['href']

                if not href.startswith('#endnote'):

                    winners.append({

                        'year'      : year,
                        'category'  : cols[i]['name'],
                        'name'      : winner.text,
                        'link'      : winner.attrs['href']
                    })

    return winners


def get_winner_nationality(winner_info_dict):

    soup = get_soup(BASE_URL, winner_info_dict['link'])

    person_data = {'name': winner_info_dict['name']}

    attr_rows = soup.select('table.infobox tr')

    for tr in attr_rows:
        try:
            attribute = tr.select_one('th').text
            if attribute.lower() == 'nationality':
                person_data[attribute] = tr.select_one('td').text
        except AttributeError:
            pass

    return person_data


def main():

    soup = get_soup(extension_url='wiki/List_of_Nobel_laureates')

    table = extract_tables_from_soup(soup)

    print table

    winners_dict = get_winners(table)

    print winners_dict

    for winner in winners_dict:

        nationality = get_winner_nationality(winner)

        person = codecs.encode(winner['name'], 'ascii', 'ignore')

        print '\n{} is from {}\n'.format(person, nationality)

if __name__ == '__main__':

    main()
