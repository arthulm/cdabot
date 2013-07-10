#!/usr/bin/python


import urllib, urllib2, urlparse, httplib

# BITLY_AUTH = 'login=pythonbitly&apiKey=R_06871db6b7fd31a4242709acaf1b6648'

class urlshortener:
  services = {
    # 'api.bit.ly': "http://api.bit.ly/shorten?version=2.0.1&%s&format=text&longUrl=" % BITLY_AUTH,
    # 'api.tr.im':   '/api/trim_simple?url=',
    # 'tinyurl.com': '/api-create.php?url=',
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


if __name__ == '__main__':
  print "use me as a module :)"


