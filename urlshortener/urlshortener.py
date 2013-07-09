#!/usr/bin/env python

import bitly_api
import sys

API_USER = "pythonbitly"
API_KEY = "R_06871db6b7fd31a4242709acaf1b6648"

b = bitly_api.BitLy(API_USER, API_KEY)

if len(sys.argv) != 2:
    print "wrong usage"
    sys.exit(0)

longurl = sys.argv[1]

response = b.shorten(longUrl=longurl)

print response['url']


