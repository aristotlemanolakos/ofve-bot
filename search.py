#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
#from our keys module (keys.py), import the keys dictionary
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

twts = api.search(q='"could of" OR "would of" OR "should of" -filter:retweets', count=100, lang="en", result_type="recent")

#list of specific strings we want to check for in Tweets
#t = ['could of']

CYELLOW = '\33[33m'
CEND = '\033[0m'
CBOLD = '\33[1m'

for s in twts:
	print(CYELLOW + CBOLD + '<' + s.user.screen_name + '>:' + CEND + ' ' + s.text + '\n')
    #print "<" + s.user.screen_name + ">: " + s.text + "\n" # Let's see what's in s.text
    #for i in t:
        #if i == s.text:
            #sn = s.user.screen_name
            #m = "@%s could *have*" % (sn)
            #s = api.update_status(m, s.id)


