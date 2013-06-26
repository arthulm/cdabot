#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from urlparse import urlparse
import socket
import string

import ircbotfunctions as ircbotfunctions

network = 'irc.hackint.eu'
port = 6667
nick = "dummbot"
channel = "#bottich"
adminmask = "armin@neon.darkbyte.org"
urlfile = "/home/armin/urllist"
fusionfile = "/home/armin/fusionlist"


irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
irc.send ( 'USER spacebot spacebot spacebot : space bot\n' )
# irc.send ( 'NICK ' + nick + '\r\n')
irc.send ( 'NICK ' + nick + '\n')

#
## function for adding url's
#def write_url(url):
#  urlfile_fd = open(urlfile, 'a')
##  print "Adding URL: " + url
#  o = urlparse(url)
#  if o.scheme == "http":
#    url = str(url)
#    urlfile_fd.write(url)
#    print "URL successfully added: " + url
#  else:
#    print "URL is not in http:// scheme, aborting!"
#  urlfile_fd.close()
#
## function for adding stuff not to forget when goin to fusion 
#def write_fusion(fusion):
#  fusionfile_fd = open(fusionfile, 'a')
#  fusionfile_fd.write(fusion)
#  fusionfile_fd.close()
#
#

# let's do shit...
while True:
  text = irc.recv(4096)
  data = text.split()
  if text.find('PING') != -1:
    print text
  if text.find('Message of the Day') != -1:
    irc.send ('JOIN ' + channel + '\r\n')
  if "PING :" in text and "No Ident response" in text:
    id = text.split('\n')[1].split(':')[1]
    print "ID for challenge/response: " + id
    irc.send('PONG :' + id)

# hide PING? PONG! events
  if data[0] != 'PING':
    # print "PING? PONG! event: " + text
    pass

# !url
  if len(data) >= 4:
    if data[3] == ':!url' and adminmask in data[0]:
       url_with_linebreak = str(data[4]) + str("\n")
       ircbotfunctions.write_url(url_with_linebreak)
       print data[4] + " has been added."

# !reload
  if len(data) >= 4:
    if data[3] == ':!reload' and adminmask in data[0]:
       reload(ircbotfunctions)
       ircbotfunctions.hallo()
       irc.send('PRIVMSG ' + channel + " reloaded functions" '\r\n')


# !fusion
  if len(data) >= 5:
    if data[3] == ':!fusion' and adminmask in data[0]:
       ircbotfunctions.hallo()
       fusion_with_linebreak = str(data[4]) + str("\n")
       ircbotfunctions.write_fusion(fusion_with_linebreak)
       nick = string.split(str(data[0]),'!')
       nn = nick[0]
       n = nn[1:]
       channel = str(data[2])
       print "!fusion command triggered in channel " + channel + " by " + n
       msg = ":Dein gewünschter Gegenstand ist: " + data[4]
       irc.send('PRIVMSG ' + channel + " " + msg + '\r\n')



# !op
  if len(data) >= 4:
    if data[3] == ':!op' and adminmask in data[0]:
      print "Op triggered by " + data[0]
      nickf = str(data[0])
      nick = string.split(nickf,'!')
      nn = nick[0]
      n = nn[1:]
      irc.send('MODE ' + channel + ' +o ' + n + '\r\n')

# !date
    if len(data) >= 4:
	    if data[3] == ':!date':
	      print "Date requested by: " + data[0]
	      nickf = str(data[0])
	      nick = string.split(nickf,'!')[0][1:]
	      irc.send('PRIVMSG ' + channel + ' ' + nick + ':' + 'es ist soundsoviel uhr.' + '\r\n')

