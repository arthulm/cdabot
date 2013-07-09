#!/usr/bin/python
# -*- coding: utf-8 -*- 

import urllib2
from BeautifulSoup import BeautifulSoup
import HTMLParser

parser = HTMLParser.HTMLParser()

# urlshortener:
import urllib, urllib2, urlparse, httplib
# BITLY_AUTH = 'login=pythonbitly&apiKey=R_06871db6b7fd31a4242709acaf1b6648'
class urlshortener:
  services = {
    # 'api.bit.ly': "http://api.bit.ly/shorten?version=2.0.1&%s&format=text&longUrl=" % BITLY_AUTH,
    # 'api.tr.im':   '/api/trim_simple?url=',
    'tinyurl.com': '/api-create.php?url=',
    'is.gd':       '/api.php?longurl='
  }
  def query(self, url):
    for shortener in self.services.keys():
      c = httplib.HTTPConnection(shortener)
      c.request("GET", self.services[shortener] + urllib.quote(url))
      r = c.getresponse()
      shorturl = r.read().strip()
      if ("Error" not in shorturl) and ("http://" + urlparse.urlparse(shortener)[1] in shorturl):
        return shorturl
      else:
        continue
    raise IOError

def urltitle(url,usermask,channel):
  urltitle_string = '::: '
  shorturl = ''
  if len(url) > 10:
    try:
      us = urlshortener()
      shorturl = us.query(url)
    except:
      print "Error while shortening URL: " + url
      pass
  if shorturl.startswith('http'):
    urltitle_string += shorturl
  # try to determine title for url:
  try:
    req = urllib2.Request(url)
    req.headers['Range'] = 'bytes=%s-%s' % (0,20000)
    f = urllib2.urlopen(req,timeout=5).read(200000)
    soup = BeautifulSoup(f)
    b = soup.title.string
    urltitle_string += ' --- ' + str(parser.unescape(b))
  except:
    print "Could not determine title for URL: " + url
    pass
  return urltitle_string

if __name__ == '__main__':
  # url = 'https://www.kernel.org/pub/linux/kernel/v3.x/linux-3.10.tar.xz'
  # url = 'http://en.wikipedia.org/wiki/Kernel.org'
  url = 'https://blog.fefe.de/'
  print urltitle2(url,'foo!foo@bar.baz','#linuxger')



