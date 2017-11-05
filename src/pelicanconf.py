#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tutov Evgenii'
SITENAME = 'yet another it blog'
SITEURL = 'https://ordinary-developer.github.io'

THEME = '/home/ivan/my_data/my_blog/themes/taman'
PELICAN_SOBER_ABOUT = 'Software developer, Russia'

PATH = 'content'

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'en'

LOCALE = ('en_US.UTF8')
DATE_FORMATS = {
    'en': '%d/%m/%Y'
}

DISQUS_SITENAME = 'ordinary-developer-github-io'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = False
