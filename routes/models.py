""" FILE DESCRIPTION : THIS FILE WILL CREATE DATABASE MODELS NEEDED FOR THE WEBSITE """

from datetime import datetime
from ..main import db # Importing db variable to create database models from main.py file from parent directory

# Creating Users Model for database
class Users(db.Model):
    ''' This Model will store users data in database '''
    # Adding Coloumns
    realNameOfUser = db.Column(db.String(250),primary_key=True)
    userName = db.Column(db.String(250),primary_key=True)
    emailOfUser = db.Column(db.String(250),nullable=False)
    passwordOfUser = db.Column(db.String(550),nullable=False)

    def __repr__(self) -> str:
        return f'{self.realNameOfUser}-{self.userName}-{self.emailOfUser}-{self.passwordOfUser}'

# Creating Question Model for database
class Question(db.model):
    ''' This Model will store details related to question in database '''
    # Adding Coloumns
    questionId = db.Column(db.String(750),primary_key=True)
    questionTitle = db.Column(db.String(250),nullable=False)
    questionDescription = db.Column(db.String(250000),nullable=False)
    userNameOfAsker = db.Column(db.String(250),nullable=False)
    dateNow = db.Column(db.DateTime,default=datetime.utcnow())
    
    def __repr__(self) -> str:
        return f'{self.questionId}-{self.questionTitle}-{self.questionDescription}'


# Creating Answers Model for database
class Answers(db.model):
    ''' This Model will store details related to answer in database '''
    # Adding Coloumns
    answerId = db.Column(db.String(750),primary_key=True)
    questionIdOfAnswer = db.Column(db.String(750),primary_key=True)
    answerDescription = db.Column(db.String(250000),nullable=False)
    userNameOfAnswerer = db.Column(db.String(250),nullable=False)
    dateNow = db.Column(db.DateTime,default=datetime.utcnow())
    
    def __repr__(self) -> str:
        return f'{self.answerId}-{self.questionIdOfAnswer}-{self.answerDescription}'