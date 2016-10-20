#!/usr/bin/env python
"""
__author__ = StackOverflow, 9/25/16
"""

import os
from os import path
from bs4 import BeautifulSoup
from urllib2 import urlopen
import urllib


# use this image scraper from the location that you want to save scraped images to

def make_soup(url):

    html = urlopen(url).read()

    return BeautifulSoup(html)


def get_images(url):

    soup = make_soup(url)

    images = [img for img in soup.findAll('img')]

    print (str(len(images)) + " images found.")
    print 'Downloading images to current working directory.'

    # compile unicode list of image links
    image_links = [each.get('src') for each in images]

    for each in image_links:
        filename = path.join(os.getcwd(), each.split('/')[-1])
        #urllib.urlretrieve(url, (url + each), filename)
        urllib.urlretrieve(url, filename)

    return image_links


def main():

    url_to_scrape = raw_input('Enter a URL to scrape, e.g. http://google.com >>>')

    get_images(url_to_scrape)


if __name__ == '__main__':
    main()
