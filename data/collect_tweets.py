from twitter_interface import YalgaarTwitterInterface
from db_interface import Tweet, engine

from sqlalchemy.orm import sessionmaker
import json

Session = sessionmaker(bind=engine)
s = Session()

y = YalgaarTwitterInterface()
tweets = y.get_data()
#print "We got total %d tweets" % len(tweets)

for text,info in tweets.items():
    favs = info['favourites_count']
    retweets = inf['retweet_count']

    t = Tweet(
            tweet = text, 
            tweet_id = info['id_str'],
            user = info['user']['screen_name'],
            data = json.dumps(info),
            weight = (favs * 1) + (retweets * 2)
        )
    s.add(t)
#now save to db
s.commit()
