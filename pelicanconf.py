#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Chris Tabone'
SITENAME = u"Chris Tabone's blog"
SITEURL = 'http://christabone.github.io'
SITELOGO = SITEURL + '/images/photo.jpg'

PATH = '/users/ctabone/Programming/christabone.github.io-src/content'

STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

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
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/christopher-tabone-34265a58'),
          ('github', 'https://github.com/christabone'),
	      ('facebook', 'https://www.facebook.com/christopher.tabone'),
          ('google', 'https://plus.google.com/+ChristopherTabone421/posts'),
          ('twitter', 'https://twitter.com/ChrisTabone'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Displaying static pages from the pages directory on the menu bar
DISPLAY_PAGES_ON_MENU = True
