from twitter_interface import YalgaarTwitterInterface
from db_interface import Tweet, engine
from dateutil import parser
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
import json

Session = sessionmaker(bind=engine)
s = Session()

def collect_tweets(tweet_type = 'mixed', hashtag = '#SaveTheInternet', limit = 100):
    y = YalgaarTwitterInterface(tweet_type = tweet_type, hashtag = hashtag, limit = limit)
    tweets = y.get_data()

    #print "We got total %d tweets" % len(tweets)

    for text,info in tweets.items():
        try:
            favs = info['favorite_count']
            retweets = info['retweet_count']

            t = Tweet(
                    tweet = text,
                    tweet_id = info['id_str'],
                    user = info['user']['screen_name'],
                    data = json.dumps(info),
                    weight = (favs * 1) + (retweets * 2),
                    tweeted_on = parser.parse(info['created_at']),
                    tweet_type = tweet_type,
                )
            s.add(t)
            s.commit()
        except IntegrityError as ie:
            s.rollback(); #This has been caused by a duplicate tweet that was encountered. Just skip.
            #print "Encountered a duplicate tweet %s" % (text.encode('utf8'))
            print "Ignoring a duplicate tweet."
            continue;
        except Exception as e:
            raise e

