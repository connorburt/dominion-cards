#!/usr/bin/env python

__author__ = 'Connor Burt'

"""

Downloads Dominion card images from the set URL, and then proceeds to rename
such cards to a more appropriate format.

"""

import scrapecards
import renamecards


def main():

    scrapecards()
    renamecards()


if __name__ == "__main__":
    main()
