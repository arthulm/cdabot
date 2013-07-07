#!/usr/bin/python

import socket

hostname = 'mpd.cdark.net'
port = 6600

class mpdclient(object):
  def __init__(self):
    pass
  def getCurrentlyPlayingSong(self):
   try:
      self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.sock.connect((hostname, port))
      b = self.sock.recvfrom(1024)
      if b[0].startswith('OK'):
        self.sock.send('currentsong\n')
        c = self.sock.recvfrom(4096)
        if c[0].startswith('OK'):
          return "Player is currently stopped."
        elements = c[0].split('\n')
        print elements
        for element in elements:
          if element.startswith('Title'):
            title = element.split(':')[1][1:]
      return title
   except:
      return "Error connecting to %s - sorry" % (hostname)

if __name__ == '__main__':
  a = mpdclient()
  print a.getCurrentlyPlayingSong()
  pass

