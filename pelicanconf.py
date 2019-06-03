#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date
from datetime import time
from datetime import datetime


AUTHOR = u'Carolin Zöbelein'
AUTHOR_AVATAR = u'/images/zoebelein_avatar.png'
SITENAME = u'Carolin Zöbelein'
SITEURL = ''
SITEURL_SOCIAL = 'https://www.carolin-zoebelein.de'
KEYWORDS = ('Carolin Zöbelein', 'Art', 'Mathematical', 'Scientist',
        'Freelancer', 'Math', 'Crytography', 'Algebra', 'Number Theory', 
        'Funding', 'Encryption', 'Privacy', 'Anonymity', 'Communication',
        'Free', 'Access', 'Information', 'Snowden', 'Digitalization',
        'Anti-Censorship', 'Circumvention', 'NSA', 'Physics', 'Exhibition',
        'Mobile', 'Free speech', 'Blocking', 'Decentralization', 'Traffic',
        'Obfuscation', 'Privacy protecting', 'Online protocols',
        'Prime numbers', 'Primes', 'Apps', 'Physics', 'Mathematical Modelling',
	'Digital', 'Mathematics', 'Math', 'Mathematical Services')

PATH = 'content'

# ******
STATIC_PATHS = ['blog', 'pages', 'images', 'files']

ARTICLE_PATHS = ['blog']
#ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
#ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{slug_dir}/{slug_subdir}/{slug}.html'
ARTICLE_URL = '{slug_dir}/{slug_subdir}/{slug}.html'

PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

SUMMARY_MAX_LENGTH = None
# ******

TIMEZONE = 'Europe/Paris'

DATE_FORMATS = {
        'en': '%Y/%m/%d',
}

DEFAULT_LANG = u'en'

# Theme
THEME = 'themes/MinimalXY'

# Theme customizations
MINIMALXY_START_YEAR = 2019
MINIMALXY_CURRENT_YEAR = date.today().year

# Icon
MINIMALXY_FAVICON = 'images/favicon.ico'

# Menu
MENUITEMS = (
    ('About', '/about.html'),
    #('Projects', '/projects.html'),
    #('Funding', '/funding.html'),
    ('Contact', '/contact.html'),
)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = u'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Index introduction
INDEX_INTRO_IMAGE = '/images/paul-m-312677-unsplash.jpg'

INDEX_RESEARCH_TITLE = 'Research'
INDEX_RESEARCH_LINK = 'https://research.carolin-zoebelein.de'
INDEX_RESEARCH_LINK_TEXT = '<i class="fas fa-superscript"></i>'
INDEX_RESEARCH_LINK_TITLE = 'Research Website'
INDEX_RESEARCH_CONTENT = 'Research. Free and Independently.'

INDEX_INTRO_TITLE = 'Welcome'
INDEX_INTRO_CONTENT = 'أهلا وسهلا Bienvenidos Bienvenue 欢迎 Karibu Willkommen'

INDEX_ART_TITLE = 'Art'
INDEX_ART_LINK = 'https://art.carolin-zoebelein.de'
INDEX_ART_LINK_TEXT = '<i class="far fa-images"></i>'
INDEX_ART_LINK_TITLE = 'Art Website'
INDEX_ART_CONTENT = 'Art. Digital and Technical.'


# PGP Keys
SIGNING_KEY = u'8F31 C7C6 E67E 9ACE 8E12 E2EF 0DE3 A4D3 BA87 2A8B'

# Social
SOCIAL = (
    ('Twitter', 'fab', 'fa', 'twitter', 'https://twitter.com/SamdneyTweet'),
    ('Blog', 'fas', 'fa', 'pencil-alt', 'https://Samdney.github.io'),
    ('Medium', 'fab', 'fa', 'medium', 'https://medium.com/@carolinzoebelein'),
    ('Flickr', 'fab', 'fa', 'flickr', 'https://www.flickr.com/photos/samdney'),
    ('Research', 'fas', 'fa', 'superscript', 'https://research.carolin-zoebelein.de'),
    ('Art', 'far', 'fa', 'images', 'https://art.carolin-zoebelein.de'),
    ('GitHub', 'fab', 'fa', 'github', 'https://github.com/Samdney'),
    ('GitLab', 'fab', 'fa', 'gitlab', 'https://gitlab.com/Samdney'),
    ('arXiv', 'ai', 'ai', 'arxiv', 'https://arxiv.org/search/?searchtype=author&query=Z%C3%B6belein%2C+C'),
)

SOCIAL_SIGNS = (
    ('Twitter', 'fab', 'fa', 'twitter'),
    ('Blog', 'fas', 'fa', 'pencil-alt'),
    ('Medium', 'fab', 'fa', 'medium'),
    ('Flickr', 'fab', 'fa', 'flickr'),
    ('Research', 'fas', 'fa', 'superscript'),
    ('Art', 'far', 'fa', 'images'),
    ('GitHub', 'fab', 'fa', 'github'),
    ('GitLab', 'fab', 'fa', 'gitlab'),
    ('arXiv', 'ai', 'ai', 'arxiv'),
    ('Website', 'fas', 'fa', 'globe'),
    ('Misc', 'fas', 'fa', 'cat'),
)

SOCIAL_PAGINATION = 5

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
