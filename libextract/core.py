"""
    libextract.core
    ~~~~~~~~~~~~~~~
    Implements the core utilities and functions in which
    libextract is built around.
"""

from operator import itemgetter
from heapq import nlargest

from lxml.html import parse, HTMLParser
from lxml import etree
from statscounter import StatsCounter

__all__ = ['parse_html', 'pipeline']

SELECT_PARENTS = '//body//*/..'

TOP_FIVE = 5

def parse_html(fileobj, encoding):
    """
    Given a file object *fileobj*, get an ElementTree instance.
    The *encoding* is assumed to be utf8.
    """
    parser = HTMLParser(encoding=encoding, remove_blank_text=True)

    try:
        # this is done because lxml sometimes (yes, only sometimes)
        # does not like the fact that fileobj is a string and not a file
        # object. See http://stackoverflow.com/a/8917972 for more info.
        # note that, if this method does not work, we fallback to parse.
        return etree.fromstring(fileobj, parser)
    except ValueError:
        return parse(fileobj, parser)


def pipeline(data, funcs):
    """
    Pipes *functions* onto a given *data*, where the result
    of the previous function is fed to the next function.
    """
    for func in funcs:
        data = func(data)
    return data


def select(etree, query=SELECT_PARENTS):
    return etree.xpath(query)


def measure(nodes):
    return [(node, StatsCounter([child.tag for child in node]))
            for node in nodes]


def rank(pairs, key=lambda x: x[1].most_common(1)[0][1],
         count=TOP_FIVE):
    return nlargest(count, pairs, key=key)


def finalise(ranked):
    for node, metric in ranked:
        yield node
