# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 12:18:46 2019

@author: ASUS
"""

## Search 5 hashtag

from config import create_api
import pandas

def main(hashtags):
    api = create_api()
    hashtag_tweets = []
    
    for hashtag in hashtags:
        for tweet in api.search(q=hashtag, lang="en", rpp=50, tweet_mode="extended"):
            hashtag_tweets.append(tweet._json)
    
    print(hashtag_tweets)
    
    df = pandas.DataFrame(hashtag_tweets)
    df.to_csv("spyder_hashtag.csv")

if __name__ == "__main__":
    hashtags = ["#google", "#100DaysOfCode", "#python", "#privacy", "#javascript"]
    main(hashtags)

    
