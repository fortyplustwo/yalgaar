from flask.ext.frozen import Freezer
from yalgaar import app

f = Freezer(app)
if __name__ == '__main__':
    f.freeze()

