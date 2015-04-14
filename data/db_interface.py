from sqlalchemy import create_engine
engine = create_engine('sqlite:///test.db', echo=True)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String, Text, Boolean

class Tweet(Base):
    __tablename__ = 'tweets'

    id = Column(Integer, primary_key=True)
    tweet = Column(String(395), unique=True) #for the tweet of 140 chars + an URL of 255 chars max
    tweet_id = Column(String(100))
    user = Column(String(100))
    weight = Column(Integer(3)) #Equals 1xNumber_of_Favs 2xNumber_of_Retweets. Otherwise 0
    data = Column(Text)
    submitted = Column(Boolean, default = False) #If a Tweet has been manually submitted using our special mechanism, this is True

    #json_blob = db.Column(db.string() # a blob for storing all data about the tweet that we might use later
  
    def __repr__(self):
        return '%s : %s' % (self.username, self.tweet)

Base.metadata.create_all(engine)

