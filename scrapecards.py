#!/usr/bin/env python

__author__ = 'Connor Burt'

"""

Scrapes card images from designated URL.

"""

import os
import shutil

from lxml import html
import requests


page = requests.get(
    'http://wiki.dominionstrategy.com/index.php/Template:Navbox_Cards')
tree = html.fromstring(page.content)

base_url = 'http://wiki.dominionstrategy.com'
card_links = tree.xpath('//span[@class="card-popup"]/span/img/@src')

directory = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         'cards')


def scrapecards():

    if not os.path.isdir(directory):
        os.makedirs(directory)

    for link in card_links:
        link = link.replace('/thumb', '').split('.jpg')
        link = '{}{}'.format(link[0], '.jpg')
        r = requests.get(base_url+link, stream=True)
        filename = os.path.join(directory, link.split('/')[4])

        if r.status_code == 200:

            with open(filename, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)


if __name__ == "__main__":
    scrapecards()
