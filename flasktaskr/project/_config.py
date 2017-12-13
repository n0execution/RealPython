import os

#grab the folder path where this script locates
basedir = os.path.abspath(os.path.dirname(__file__))



DATABASE = 'flasktaskr.db'

WTF_CSRF_ENABLED = True
SECRET_KEY = os.urandom(24)

DEBUG = False
DATABASE_PATH = os.path.join(basedir, DATABASE)


#define full path for the database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH