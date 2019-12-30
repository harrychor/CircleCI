import unittest
import pymysql
from flask import Flask, jsonify, request 
from flask_sqlalchemy import SQLAlchemy
import flask

app = Flask(__name__)
# insert the data into mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:P@ssw0rd123@127.0.0.1/twitter'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Account_created(db.Model): # create table Account_created
    __tablename__ = 'Account_created'
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(50))
    created_at = db.Column('created_at', db.DateTime)

    def __init__(self, username, created_at):
        self.username = username
        self.created_at = created_at

class Twitter(db.Model): # create table twitter
    __tablename__ = 'Twitter'
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(50))
    DATE = db.Column('DATE', db.Date)
    followers_count = db.Column('followers_count', db.Integer)
    following_count = db.Column('following_count', db.Integer)
    tweet_count = db.Column('tweet_count', db.Integer)
    like_count = db.Column('like_count', db.Integer)
    
    def __init__(self, username, DATE, followers_count, following_count, tweet_count, like_count):
        self.username = username
        self.DATE = DATE
        self.followers_count = followers_count
        self.following_count = following_count
        self.tweet_count = tweet_count
        self.like_count = like_count

class TestStringMethods(unittest.TestCase):

    def test_insert_Account_created(self):
        data = Account_created("test","1970-01-01")
        db.session.add(data)
        db.session.commit()
        self.assertTrue(data)

    def test_insert_Twitter(self):
        insdata = Twitter("test","2019-12-30","721","69","101","64")
        db.session.add(insdata)
        db.session.commit()

    def test_isitexist_Account_created(self):
        exists = db.session.query(Account_created.id).filter_by(username="test").scalar() is not None
        dateexist = db.session.query(Twitter.id).filter_by(DATE = "2019-12-30", username = "test").scalar() is not None
        db.session.commit()
        
        
if __name__ == '__main__':
    unittest.main()
