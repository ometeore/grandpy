import os


SECRET_KEY = '#d#JCqTTW\nilK\\7m\x0bp#\tj~#H'
FB_APP_ID = 1200420960103822

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'grandpy.db')