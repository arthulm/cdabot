#!/usr/bin/python
# -*- coding: utf-8 -*- 

import urllib2
from BeautifulSoup import BeautifulSoup
import HTMLParser

parser = HTMLParser.HTMLParser()

def urltitle(url,usermask,channel):
  print "urltitle was called on: " + url
  soup = BeautifulSoup(urllib2.urlopen(url,timeout=3))
  b = soup.title.string
  b = b.encode('ascii','ignore')
  return "::: " + str(parser.unescape(b).encode('utf-8'))

if __name__ == '__main__':
  print urltitle('http://www.sueddeutsche.de/panorama/posse-in-nrw-um-leben-des-brian-sie-wollten-doch-nur-einen-film-schauen-1.1714190','foo!foo@bar.baz','#linuxger')



