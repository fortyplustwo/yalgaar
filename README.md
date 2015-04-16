yalgaar
=======

Makes available Tweets for trending on Twitter, Facebook and WhatsApp.
Please join the movement and help keep Internet an equal and free (as in freedom) place!

Why?
----

Yalgaar has been created to help the [save the Internet](http://savetheinternet.in) movement
by helping trend the various hashtags and tweets related to it.

Since, Twitter does not count re-tweets towards the trending count, we need to 
make available "new" tweets. Though one can go to Twitter search results for a
page, copy the tweets and paste them and tweet them again, we thought this
tool can make it easier! :)

History
-------

The precursor to this project was the wonderful spreadsheet designed by /u/saptarshi on
http://goo.gl/mb81Jo which was used to trend SaveTheInternet and RightToPlay in the 
beginning of the movement.

Contributing
------------

This project uses SQLAlchemy, Flask, Jinja, Frozen-Flask, Twython and python-dateutils.

* Set up a virtual environment by using `requirements.txt` and activate it
* Get your own API KEY and API SECRET from Twitter by creating an app and put it in [yalgaar/data/settings.py](https://github.com/knightsamar/yalgaar/blob/master/yalgaar/data/settings.py.example)
* Setup a database in PostgreSQL and put credentials in `yalgaar/data/settings.py`
* If you are using MySQL or SQLite3, just [change the engine](http://docs.sqlalchemy.org/en/rel_0_9/core/engines.html#sqlalchemy.create_engine) in `yalgaar/data/db_interface.py`
* Run `run.py` for running the server.
* Run `freeze.py` for generating a static version of the site inside `yalgaar/build/`
* Send a pull request :)

About the name
--------------

Yalgaar is Urdu for attack. We don't mean to attack anyone physically or verbally.
This is just to help trend an already popular sentiment on social networks.
And I didn't even know there was a Bollywood film with that name!

