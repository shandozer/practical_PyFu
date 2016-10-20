#!/usr/bin/env python
"""
__author__ = , 9/13/16
"""

import sys
from bs4 import BeautifulSoup
import urllib2
import codecs

VERSION = '0.1.0'

BASE_URL = 'http://en.wikipedia.org/'


def get_soup(base_url=BASE_URL, extension_url=''):
    """Grab all elements from given URL page"""

    info = urllib2.urlopen(base_url + extension_url)

    return BeautifulSoup(info, "lxml")


def extract_tables_from_soup(soup):
    """Single-out a certain table element given page element 'soup' """

    # tables = soup.select('table.sortable.wikitable')

    table = soup.select_one('table.sortable.wikitable')

    return table


def get_column_titles(table):
    """Takes table element and looks for headers and links, returning list of dicts for each column header"""

    cols = []

    for th in table.select_one('tr').select('th')[1:]:
        link = th.select_one('a')
        if link:
            cols.append({'name': link.text, 'href': link.attrs['href']})
        else:
            cols.append({'name': th.text, 'href': None})

    return cols


def get_winners(table):
    """takes table soup and returns list of dicts with winner info"""

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

    nationality = {'name': winner_info_dict['name']}

    attr_rows = soup.select('table.infobox tr')

    for tr in attr_rows:
        try:
            attribute = tr.select_one('th').text
            if attribute.lower() == 'nationality':
                nationality[attribute] = tr.select_one('td').text
        except AttributeError:
            pass

    return nationality


def main():

    soup = get_soup(extension_url='wiki/List_of_Nobel_laureates')

    table = extract_tables_from_soup(soup)

    winners_list = get_winners(table)

    try:

        for winner in sorted(winners_list):

            category = codecs.encode(winner['category'], 'ascii', 'ignore')

            person = codecs.encode(winner['name'], 'ascii', 'ignore')

            year = codecs.encode(str(winner['year']), 'ascii', 'ignore')

            print '\n{} || {} || {}\n'.format(person, category, year)

    except KeyboardInterrupt:
        print 'Exiting...'
        sys.exit()

if __name__ == '__main__':

    main()
