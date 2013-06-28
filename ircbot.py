#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from urlparse import urlparse
import socket
import string
import datetime

# import ircbotfunctions as ircbotfunctions

network = 'irc.hackint.eu'
port = 6667
nick = "bottich"
username = "bottich"
channel = "#bottich"
adminmask = "armin@neon.darkbyte.org"
# urlfile = "/home/armin/urllist"
# fusionfile = "/home/armin/fusionlist"

# print debug messages?
debug = True

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((network, port))
sock.send('USER ' + username + ' ' + username + ' ' + username + ' ' + username + ' : boddisch\n')
sock.send('NICK ' + nick + '\r\n')

class CommandHandler(object):
  def __init__(self,line):
    print line

class MessageHandler(object):
  def __init__(self):
    print "new message handler instance created"
  def processMessage(self, line):
    # print "DEBUG: command handler got line: " + line
    if line.startswith('PING :'):
      id = line.split(':')[1]
      return 'PONG :' + id
    if line.rstrip().endswith(':End of /MOTD command.'):
      if debug:
        print "successfully connected, joining channels."
      return "JOIN " + channel + '\r\n'
      joined = True
    if line.rstrip().startswith(':') and ' PRIVMSG #' in line and line.split(' ')[3].startswith(':!'):
      print "we got a command here: " + line
      usermask, messagetype, chan, command = line.split(' ')
      # strip unwanted stuff
      usermask = usermask[1:]
      command = command[1:]
      print "user " + usermask + " requested " + command + " comand on channel " + chan
    else:
      if debug:
        print "=== " + line
    
class ChunkHandler(object):
  def __init__(self,sock,messagehandler=MessageHandler()):
    self.buffer = ''
    self.ircsocket = sock
    self.messagehandler = messagehandler
  def progressChunk(self):
    # fill buffer until we have a newline character
    while not '\n' in self.buffer:
      self.data = self.ircsocket.recv(4096)
      self.buffer = self.buffer + self.data
      self.buffer = self.buffer.replace('\r\n','\n')
    lines = self.buffer.split('\n')
    if len(lines) == 1:
      line = lines[0]
      self.buffer = ''
    else:
      line = lines[0]
      self.buffer = '\n'.join(lines[1:])
    response = self.messagehandler.processMessage(line)
    if type(response) is str:
      self.ircsocket.send(response + '\r\n')

chunkhandler = ChunkHandler(sock)

while True:
  chunkhandler.progressChunk()


# 
# 
# 
# # let's do shit...
# while True:
#   text = ircsocket.recv(4096)
#   data = text.split()
#   if text.find('PING') != -1:
#     print text
#   if text.find('Message of the Day') != -1:
#     ircsocket.send ('JOIN ' + channel + '\r\n')
#   if "PING :" in text and "No Ident response" in text:
#     id = text.split('\n')[1].split(':')[1]
#     print "ID for challenge/response: " + id
#     ircsocket.send('PONG :' + id)
# 
# # hide PING? PONG! events
#   if data[0] != 'PING':
#     # print "PING? PONG! event: " + text
#     pass
# 
# # !url
#   if len(data) >= 4:
#     if data[3] == ':!url' and adminmask in data[0]:
#        url_with_linebreak = str(data[4]) + str("\n")
#        ircbotfunctions.write_url(url_with_linebreak)
#        print data[4] + " has been added."
# 
# # !reload
#   if len(data) >= 4:
#     if data[3] == ':!reload' and adminmask in data[0]:
#        reload(ircbotfunctions)
#        ircbotfunctions.hallo()
#        ircsocket.send('PRIVMSG ' + channel + " reloaded functions" '\r\n')
# 
# 
# # !fusion
#   if len(data) >= 5:
#     if data[3] == ':!fusion' and adminmask in data[0]:
#        ircbotfunctions.hallo()
#        fusion_with_linebreak = str(data[4]) + str("\n")
#        ircbotfunctions.write_fusion(fusion_with_linebreak)
#        nick = string.split(str(data[0]),'!')
#        nn = nick[0]
#        n = nn[1:]
#        channel = str(data[2])
#        print "!fusion command triggered in channel " + channel + " by " + n
#        msg = ":Dein gewünschter Gegenstand ist: " + data[4]
#        ircsocket.send('PRIVMSG ' + channel + " " + msg + '\r\n')
# 
# 
# 
# # !op
#   if len(data) >= 4:
#     if data[3] == ':!op' and adminmask in data[0]:
#       print "Op triggered by " + data[0]
#       nickf = str(data[0])
#       nick = string.split(nickf,'!')
#       nn = nick[0]
#       n = nn[1:]
#       ircsocket.send('MODE ' + channel + ' +o ' + n + '\r\n')
# 
# # !date
#     if len(data) >= 4:
# 	    if data[3] == ':!date':
# 	      print "Date requested by: " + data[0]
# 	      nickf = str(data[0])
# 	      nick = string.split(nickf,'!')[0][1:]
# 	      ircsocket.send('PRIVMSG ' + channel + ' :' + nick + ': ' + 'es ist ' + datetime.datetime.isoformat(datetime.datetime.now()) + '' + '\r\n')
 
