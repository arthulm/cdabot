#!/usr/bin/python

from calcer import calcer

c = calcer.Calcer()
m = c.getCalc('test')
if not len(m) == 0:
    print m
else:
    print "no such entry"




