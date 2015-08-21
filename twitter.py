import tweepy
import private
from random import randint, choice
from alchemyapi import AlchemyAPI
from chain import *

auth = tweepy.OAuthHandler(private.consumer_key, private.consumer_secret)
auth.set_access_token(private.access_token, private.access_token_secret)
api = tweepy.API(auth)

def createTwiiterSource(search): #searches 500 tweets based on results from 'search'
    tweets = tweepy.Cursor(api.search, [q=search, lang='en']).items(500)
    source = ""
    for tweet in tweets:
        source = source + tweet.text + " "
    source = source.split()
    for index, word in enumerate(source):
        if word[0] == "@" or word[0] == "#": #remove references to actual users
            del source[index]
    return " ".join(source)

def createTweets(source, num): #num is number of tweets to create
    words = createDict(source, 2) #state size of 2 allows for more combinations as tweets are small
    tweets = []
    api = AlchemyAPI()
    for x in range(0, num): #at most 50% chance of using a hashtag
        if randint(0,1) == 0:
            tweet = generateText(words, 2, choice(range(100,140)))
            tweets.append(tweet)
        else:
            tweet = generateText(words, 2, choice(range(80,120)))
            response = api.concepts('text', tweet)
            if response['status'] == 'OK':
                hashtag = " #" + response['concepts'][0]['text'].replace(" ", "")
                if len(hashtag) <= 140 - len(tweet):
                    tweet = tweet + hashtag
            tweets.append(tweet)
    return tweets
