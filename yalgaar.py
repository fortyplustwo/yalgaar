from flask import Flask, request, render_template
from settings import *
from data.db_interface import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

app = Flask(__name__)
#app.config.from_object(__name__)

@app.route('/')
def index():
    #TODO: Create a frozen-flask installation every 30 minutes and forward connections to it.
    
    Session = sessionmaker(bind=engine)
    s = Session()

    tweets = s.query('tweet', 'user', 'tweet_id').\
                from_statement(text("select * from tweets")).all()
    

    print tweets

    return render_template('tweets.html', tweets = tweets)

if __name__ == '__main__':
    app.run(debug=True)
