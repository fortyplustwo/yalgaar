from sqlalchemy import create_engine
from settings import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME
engine = create_engine('postgresql+psycopg2://%s:%s@%s/%s' % (DB_USER, DB_PASSWORD, DB_HOST, DB_NAME),
                        echo=True,
                    )
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String, Text, Boolean, SmallInteger, DateTime, Enum
from sqlalchemy.dialects.postgresql import JSON

class Tweet(Base):
    __tablename__ = 'tweets'

    id = Column(Integer, primary_key=True)
    tweet = Column(String(395), unique=True) #for the tweet of 140 chars + an URL of 255 chars max
    tweet_id = Column(String(100))
    user = Column(String(100))
    weight = Column(SmallInteger) #Equals 1xNumber_of_Favs 2xNumber_of_Retweets. Otherwise 0
    data = Column(JSON)
    tweeted_on = Column(DateTime(timezone=True))
    tweet_type = Column(Enum('popular','recent','submitted', name = 'tweet_type'))

    #json_blob = db.Column(db.string() # a blob for storing all data about the tweet that we might use later
  
    def __repr__(self):
        return '%s : %s' % (self.user, self.tweet)

Base.metadata.create_all(engine)

