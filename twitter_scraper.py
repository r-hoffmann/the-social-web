
import pandas as pd
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

tweet_ids = []
for month in ['2018-01', '2018-02', '2018-12', '2019-05', '2019-09', '2019-10', '2019-11', '2019-12', '2020-01', '2020-02']:
    with open(f'{month}_tweetIds_0.txt') as f:
        tweet_ids += [x.strip() for x in f.readlines()]
print(len(tweet_ids))

print(tweet_ids[0])

l = len(tweet_ids)
tweets = []
for i, tweet_id in enumerate(tweet_ids):
    if i < 5500 or i >= 30300:
        link = f"https://twitter.com/ethstatuts/status/{tweet_id}"
        response = requests.get(link)

        tweet = {
            'id': tweet_id,
            'content': response.text
        }
        print(i)
        tweets.append(tweet)
        if (i+1) % 100 == 0:
            print(f'{i}/{l} done')
            tweets_df = pd.DataFrame(tweets)
            tweets_df.to_csv(f'tweets_{i}.csv')
            tweets = []
tweets_df = pd.DataFrame(tweets)
tweets_df.to_csv(f'tweets_{i}.csv')
tweets = []
