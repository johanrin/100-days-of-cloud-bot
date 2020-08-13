#!/usr/bin/env python
# tweepy-bots/bots/favretweet.py

import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def fav_retweet(api):
    logger.info("Retrieving, marking as Liked and retweeting")
    for tweet in tweepy.Cursor(api.search, q="#100DaysOfCloud -filter:retweets -fiverr", lang ="en").items(5):
        if not tweet.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.favorite()
            except Exception as e:
                logger.error("Error on fav", exc_info=True)
        if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                tweet.retweet()
            except Exception as e:
                logger.error("Error on fav and retweet", exc_info=True)
        time.sleep(5)

def main():
    api = create_api()
    while True:
        fav_retweet(api)
        logger.info("Waiting...")
        time.sleep(60)


if __name__ == "__main__":
    main()
