#!/usr/bin/python

import urllib2
from BeautifulSoup import BeautifulSoup

def urltitle(url,usermask,channel):
  print "urltitle was called on: " + url
  title = BeautifulSoup(urllib2.urlopen(url,timeout=3)).title.string
  title = str(title)
  return "::: " + title

