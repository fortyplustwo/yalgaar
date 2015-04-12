from sqlalchemy import create_engine
engine = create_engine('sqlite:///test.db', echo=True)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String

class Tweet(Base):
    __tablename__ = 'tweets'

    id = Column(Integer, primary_key=True)
    tweet = Column(String(395), unique=True) #for the tweet of 140 chars + an URL of 255 chars max
    user = Column(String(100), unique=True)
    #json_blob = db.Column(db.string() # a blob for storing all data about the tweet that we might use later
  
    def __repr__(self):
        return '%s : %s' % (self.username, self.tweet)

Base.metadata.create_all(engine)

