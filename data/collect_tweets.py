from twitter_interface import YalgaarTwitterInterface
from db_interface import Tweet, engine

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
s = Session()

y = YalgaarTwitterInterface()
tweets = y.get_data()
import pdb
pdb.set_trace()
#print "We got total %d tweets" % len(tweets)

for text,info in tweets.items():
    t = Tweet(
            tweet = text, 
            user = '%s' % (info['user']['screen_name'])
        )
    s.add(t)
#now save to db
s.commit()   
