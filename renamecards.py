#!/usr/bin/env python

__author__ = 'Connor Burt'

import os

"""

Renames cards in the "cards" directory.

"""


directory = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         'cards')
names = os.listdir(directory)


def renamecards():

    for name in names:
        new_name = name.lower()

        if '%27' in name:
            new_name = new_name.replace('%27', '')

        if '_' in name:
            new_name = new_name.replace('_', '-')

        os.rename('{}/{}'.format(directory, name),
                  '{}/{}'.format(directory, new_name))


if __name__ == "__main__":
    renamecards()
