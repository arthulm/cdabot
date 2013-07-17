#!/usr/bin/python
# -*- coding: utf-8 -*- 

import urllib2
from BeautifulSoup import BeautifulSoup
import HTMLParser
import time

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

class UrltitleException(Exception):
  pass

def urltitle(url,usermask,channel):
    timeout_duration=3
    '''This function will spwan a thread and run the given function using the args, kwargs and 
    return the given default value if the timeout_duration is exceeded 
    ''' 
    import threading
    class InterruptableThread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.result = "ERROR"
        def run(self):
            try:
                self.result = urltitle_real(url,usermask,channel)
            except Exception, e:
                print "exception occured while trying to determine url via urltitle_real function: " + str(e)
                self.result = "ERROR"
    it = InterruptableThread()
    it.start()
    it.join(timeout_duration)
    if it.isAlive():
        print "InterruptableThread is alive"
        if not "ERROR" in it.result:
            return it.result
        else:
            raise UrltitleException('InterruptableThread alive but ERROR in it.result')
    else:
        print "InterruptableThread is not alive"
        if not "ERROR" in it.result:
            return it.result
        else:
            raise UrltitleException('InterruptableThread alive but ERROR in it.result')

def urltitle_real(url,usermask,channel):
  print "Trying to determine title for url: " + url
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
    f = urllib2.urlopen(req,timeout=5)
    soup = BeautifulSoup(f)
    b = soup.title.string
    b = parser.unescape(b)
    b = b.encode('latin1','ignore')
    urltitle_string += ' --- ' + b
  except Exception, e:
    print "Could not determine title for URL: " + url + " - error: " + str(e)
  return urltitle_string

if __name__ == '__main__':
  # url = 'https://www.kernel.org/pub/linux/kernel/v3.x/linux-3.10.tar.xz'
  # url = 'http://en.wikipedia.org/wiki/Kernel.org'
  url = 'https://blog.fefe.de/'
  print urltitle2(url,'foo!foo@bar.baz','#linuxger')



