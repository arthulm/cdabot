#!/usr/bin/python

import urllib2
from BeautifulSoup import BeautifulSoup

def urltitle(url):
  title = BeautifulSoup(urllib2.urlopen(url,timeout=3)).title.string
  return "::: " + title

