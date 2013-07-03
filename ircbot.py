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
nick = "cdabot"
username = "cdabot"
channel = "#chaos-darmstadt"
adminmask = "armin@neon.darkbyte.org"

# print debug messages?
debug = True


class CommandHandler(object):
  def __init__(self,line):
    print line


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

  def processMessage(self, rawline):
    # strip unwanted newrawline characters:
    # rawline = rawline.rstrip()
    # print ":: processMessage rawline :: " + rawline
    if rawline.startswith('PING :'):
      id = rawline.split(':')[1]
      return self.handlePing(id)
    if rawline.endswith(':End of /MOTD command.'):
      return self.handleMotd()
    ### RAW: :spaceboyz.net NOTICE AUTH :*** Looking up your hostname...
    messagetype = rawline.split(' ',1)[1].split(':')[0].lstrip().rstrip()
    if messagetype == "NOTICE AUTH":
      print "We got a notice auth line here."
    elif messagetype.startswith("372"):
      # print "MOTD line: " + rawline
      pass
    elif messagetype.split(' ')[0] == "PRIVMSG":
      print "This line should be handled by our privmsg-handler: " + rawline
      try:
        self.handlePrivmsg(rawline)
      except Exception, e:
        print "Critical error while trying to progress line via the handlePrivmsg method: " + str(e)
    else:
      print "We got an unknown messagetype here: "
      print "--- Raw Line: " + rawline

# handle methods:

  def handlePing(self,id):
    return 'PONG :' + id

  def handleMotd(self):
    return 'JOIN ' + channel + '\r\n'

  def handlePrivmsg(self,rawline):
    messageComponents = rawline.split(':')
    attr = messageComponents[1]
    chatline = messageComponents[2]
    print "handlePrivmsg attr: " + attr
    a = attr.split(' ')
    usermask = a[0]
    messagetype = a[1]
    channel = a[2]
    # print "Usermask: %s, MSG-Type: %s, Channel: %s, Text: %s" % (usermask, messagetype, channel, chatline)
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
        self.sock.send('PRIVMSG ' + channel + ' :' + ircmessage + '\r\n')
      except:
        self.sock.send('PRIVMSG ' + channel + ' :' + 'something went terribly wrong' + '\r\n')
    else:
      self.sock.send('PRIVMSG ' + channel + ' :' + 'no such command' + '\r\n')


ircconnection = IrcConnection()
ircconnection.run()


