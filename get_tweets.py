import os
import memcache
from twitter import Api

MAX_TWEETS = 10
TAGS = ['#vldc','#gdgvl']

if __name__ == '__main__':

    MEMCACHE_SERVER=os.getenv("MEMCACHE_SERVER", None)
    mc = memcache.Client([MEMCACHE_SERVER])
    api = Api(os.environ["CONSUMER_KEY"],
              os.environ["CONSUMER_SECRET"],
              os.environ["ACCESS_TOKEN"],
              os.environ["ACCESS_TOKEN_SECRET"])

    for tweet in api.GetStreamFilter(track=TAGS):
        tweets = mc.get("last_tweets") or []
        tweets = sorted(tweets, key=lambda x: x["created_at"], reverse=True)[:MAX_TWEETS-1]
        tweets = [tweet] + tweets
        mc.set("last_tweets", tweets)

