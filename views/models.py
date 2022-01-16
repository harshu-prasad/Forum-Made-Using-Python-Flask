""" FILE DESCRIPTION : THIS FILE WILL CREATE DATABASE MODELS NEEDED FOR THE WEBSITE """

from datetime import datetime
from . import db # Importing db variable to create database models from main.py file from parent directory
from flask_login import UserMixin # Importing UserMixin from flask_login module for loggin in users

# Creating Users Model for database
class User(db.Model, UserMixin):
    ''' This Model will store users data in database '''
    # Adding Coloumns
    userName = db.Column(db.String(1000),primary_key=True)
    realNameOfUser = db.Column(db.String(250),nullable=False)
    emailOfUser = db.Column(db.String(250),nullable=False,unique=True) #Adding unique=True to add only unique emails in database
    passwordOfUser = db.Column(db.String(1000),nullable=False)

    def get_id(self):
        ''' This function will override the default properties of get_id under the User Class '''
        return (self.userName)

# Creating Question Model for database
class Question(db.Model):
    ''' This Model will store details related to question in database '''
    # Adding Coloumns
    questionId = db.Column(db.String(1000),primary_key=True)
    questionTitle = db.Column(db.String(250),nullable=False)
    questionDescription = db.Column(db.String(250000),nullable=False)
    userNameOfAsker = db.Column(db.String(1000),nullable=False)
    realNameOfAsker = db.Column(db.String(250),nullable=False)
    categoryId = db.Column(db.String(300),nullable=False)
    dateNow = db.Column(db.DateTime,default=datetime.utcnow())

# Creating Answers Model for database
class Answer(db.Model):
    ''' This Model will store details related to answer in database '''
    # Adding Coloumns
    answerId = db.Column(db.String(1000),primary_key=True)
    questionIdOfAnswer = db.Column(db.String(1000),nullable=False) # This is the id of the questio of which is the answer
    answerDescription = db.Column(db.String(250000),nullable=False)
    userNameOfAnswerer = db.Column(db.String(1000),nullable=False)
    realNameOfAnswerer = db.Column(db.String(250),nullable=False)
    dateNow = db.Column(db.DateTime,default=datetime.utcnow())

# Creating Category Models for Database
class Category(db.Model):
    ''' This class will create a model for the categories of the website '''
    # Adding Coloumns
    categoryId = db.Column(db.String(300),primary_key=True)
    categoryName = db.Column(db.String(1000),nullable=False)
    categoryDescription = db.Column(db.String(10000),nullable=False)
    categoryImage = db.Column(db.String(1000),nullable=True)