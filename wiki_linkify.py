"""
How to use
>>> from wiki_linkify import wiki_linkify
>>> wiki_linkify('I <3 CamelCase!')
'I <3 <a href="/CamelCase">CamelCase</a>!'
"""

import re

def _replace(word):
    """
    Replaces words with links
    """
    return '<a href="/%s">%s</a>' % (word.group(0), word.group(0))

def wiki_linkify(string):
    """
    Finds CamelCase words within a given string and calls _replace to Replace
    only those words with their equivalent links
    """
    return re.sub('([A-Z][a-z]+){2,}', _replace, string)

if __name__ == '__main__':
    print wiki_linkify('I work at DigitalCrafts. I am SuperAwesome.')
