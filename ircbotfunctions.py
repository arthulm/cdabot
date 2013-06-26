#!/usr/bin/python

urlfile = "/home/armin/urllist"
fusionfile = "/home/armin/fusionlist"

def hallo():
  print "Hallo Welt 4"

# function for adding url's
from urlparse import urlparse
def write_url(url):
  urlfile_fd = open(urlfile, 'a')
#  print "Adding URL: " + url
  o = urlparse(url)
  if o.scheme == "http":
    url = str(url)
    urlfile_fd.write(url)
    print "URL successfully added: " + url
  else:
    print "URL is not in http:// scheme, aborting!"
  urlfile_fd.close()

# function for adding stuff not to forget when goin to fusion 
def write_fusion(fusion):
  fusionfile_fd = open(fusionfile, 'a')
  fusionfile_fd.write(fusion)
  fusionfile_fd.close()



