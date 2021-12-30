""" FILE DESCRIPTION : THIS FILE WILL CREATE DATABASE MODELS NEEDED FOR THE WEBSITE """

from ..main import db # Importing db variable to create database models from main.py file from parent directory

class Users(db.Model):
    # Adding Coloumns
    realNameOfUser = db.Column(db.String(250),primary_key=True)
    emailOfUser = db.Column(db.String(250),nullable=False)
    passwordOfUser = db.Column(db.String(550),nullable=False)

    def __repr__(self) -> str:
        return f'{self.realNameOfUser}-{self.emailOfUser}-{self.passwordOfUser}'