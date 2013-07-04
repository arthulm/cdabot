#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from urlparse import urlparse
import socket
import string
import datetime

import ircbotfunctions as ircbotfunctions

network = 'irc.hackint.eu'
port = 6667
nick = "cda2bot"
username = "cdabot"
# testing channel
channel = "#cdabot"
# channel = "#chaos-darmstadt"
adminmask = "armin@neon.darkbyte.org"

class IrcConnection(object):

  def __init__(self):
    print "Connecting to " + network + ":" + str(port)
    self.buffer = ''
    # connect to IRC
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.connect((network, port))
    self.sock.send('USER ' + username + ' ' + username + ' ' + username + ' ' + username + ' : boddisch\n')
    self.sock.send('NICK ' + nick + '\r\n')
    # self.messagehandler = MessageHandler()

  def run(self):
    while True:
      self.progressChunk()

  def progressChunk(self):
    # fill buffer until we have a newline character
    while not '\n' in self.buffer:
      # read 4k data from socket
      data = self.sock.recv(4096)
      self.buffer = self.buffer + data
      self.buffer = self.buffer.replace('\r\n','\n')
    lines = self.buffer.split('\n')
    if len(lines) == 1:
      rawline = lines[0]
      self.buffer = ''
    else:
      rawline = lines[0]
      self.buffer = '\n'.join(lines[1:])
    response = self.processMessage(rawline)
    if type(response) is str:
      # write response to socket
      self.sock.send(response + '\r\n')

# :chaotiker!~chaos@2001:41b8:83f:4243:230:18ff:fea5:8f65 PRIVMSG #cdabot :!hallo

  def processMessage(self, rawline):
    # debugging:
    print "processMessage got rawline: " + rawline

    # PING/PONG:
    if rawline.startswith('PING :'):
      id = rawline.split(':')[1]
      return self.handlePing(id)

    # End of MOTD:
    if rawline.endswith(':End of /MOTD command.'):
      return self.handleMotd()
    messagetype = rawline.split(' ',1)[1].split(' :')[0].lstrip().rstrip()

    # NOTICE AUTH:
    if messagetype == "NOTICE AUTH":
      print "We got a notice auth line here."

    # MOTD:
    elif messagetype.startswith("372"):
      pass

    # PRIVMSG:
    elif messagetype.split(' ')[0] == "PRIVMSG":
      # print "This line should be handled by our privmsg-handler: " + rawline
      try:
        self.handlePrivmsg(rawline)
      except Exception, e:
        print "Critical error while trying to progress line via the handlePrivmsg method: " + str(e)
    else:
      print "We got an unknown messagetype here: "
      print "--- Raw Line: " + rawline

# handle methods:

  def handlePing(self,id):
    print "handleping yo"
    return 'PONG :' + id

  def handleMotd(self):
    return 'JOIN ' + channel + '\r\n'

  def handlePrivmsg(self,rawline):
    usermask, messagetype, rest = rawline.split(' ', 2)
    channel, chatline = rest.split(' ', 1)
    # strip ":" character from the beginning of usermask and chatline:
    usermask = usermask[1:]
    chatline = chatline[1:]
    if chatline.startswith('!'):
      strippedline = chatline.split('!')[1]
      # if the command we got has no arguments, set args to None:
      if " " in strippedline:
        command, args = strippedline.split(' ',1)
      else:
        command, args = strippedline, None
      try:
        self.handleCommand(command,usermask,messagetype,channel,chatline,args)
      except:
        print "something went wrong when trying to call handleCommand() - please check."

  def handleCommand(self,command,usermask,messagetype,channel,chatline,args):
    reload(ircbotfunctions)
    print "handleCommand: %s %s %s %s %s %s" % (command,usermask,messagetype,channel,chatline,args)
    if hasattr(ircbotfunctions, command):
      print "%s command found in ircbotfunctions, processing." % (command)
      try:
        cmd = getattr(ircbotfunctions, command)
        ircmessage, ttymessage = cmd(usermask,messagetype,channel,chatline,args)
        print ttymessage
        if not ircmessage == None:
          self.sock.send('PRIVMSG ' + channel + ' :' + ircmessage + '\r\n')
      except:
        self.sock.send('PRIVMSG ' + channel + ' :' + 'something went terribly wrong' + '\r\n')
    else:
      # self.sock.send('PRIVMSG ' + channel + ' :' + 'no such command' + '\r\n')
      pass


ircconnection = IrcConnection()
ircconnection.run()

