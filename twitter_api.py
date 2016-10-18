import os
import sys
import tweepy



def get_tweets(text):
    consumer_key = "uiO2t4k8X3rdwp3TQCNBCvVI9"
    consumer_secret = "5ZkIRhP3dbwDCXr17dxWYVU5CuNovEvS76juHzoPN58QQLoA5W"
    
    access_token = "180084152-IxcMoT7aTZEZKFdBbhnEjeJ63AJCAWz6oPkupKCw"
    access_token_secret = "c5eARjp6dZD74vKrn6z0Hu2k7ZZbwq8vSLZnyceq7unVP"
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    api = tweepy.API(auth)
    
    search_text = text
    search_number = 1
    search_result = api.search(search_text, rpp=search_number)
    msg = "Maybe this can be useful for you:"
    j = 0
    for i in search_result:
        msg = msg + "\n" + i.text
        break
    
    return msg 
