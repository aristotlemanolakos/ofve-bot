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

cof = 'could of'
sof = 'should of'
wof = 'would of'

CYELLOW = '\33[33m'
CEND = '\033[0m'
CBOLD = '\33[1m'
CRED = '\33[31m'
CBLUE = '\33[34m'

tempString = ''
tempLen = 0
tempFront = ''
tempBack = ''
tempInt = 0

for s in twts:
	if cof in s.text:
		tempString = s.text
		tempLen = len(tempString)
		tempInt = tempString.find(cof)
		tempFront = tempString[0:tempInt]
		tempBack = tempString[tempInt+8:tempLen]
		print CYELLOW + CBOLD + '<' + s.user.screen_name + '>:' + CEND + ' ' + tempFront + CRED + CBOLD + cof + CEND + tempBack
	elif wof in s.text:
		tempString = s.text
		tempLen = len(tempString)
		tempInt = tempString.find(wof)
		tempFront = tempString[0:tempInt]
		tempBack = tempString[tempInt+8:tempLen]
		print CYELLOW + CBOLD + '<' + s.user.screen_name + '>:' + CEND + ' ' + tempFront + CRED + CBOLD + wof + CEND + tempBack
	elif sof in s.text:
		tempString = s.text
		tempLen = len(tempString)
		tempInt = tempString.find(sof)
		tempFront = tempString[0:tempInt]
		tempBack = tempString[tempInt+9:tempLen]
		print CYELLOW + CBOLD + '<' + s.user.screen_name + '>:' + CEND + ' ' + tempFront + CRED + CBOLD + sof + CEND + tempBack

		#print CYELLOW + CBOLD + '<' + s.user.screen_name + '>:' + CEND + ' ' + s.text


