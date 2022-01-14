from flask import Blueprint,request,redirect,flash
from . import db # Importing Database Variable
from .models import User # Importing User from models.py to access Name of User
from .models import Question
import uuid
# from flask.typing import StatusCode

askQuestion = Blueprint('askQuestion',__name__,template_folder='templates') # Creating Blueprint to adress /askQuestion endpoint

@askQuestion.route('/<string:profileUserName>',methods=['POST'])
def askQuestionFunction(profileUserName):
    userData = User.query.filter_by(userName=profileUserName).first() # Getting Data of User
    askedQuestionId = uuid.uuid4().hex # Creating Question Id of Question
    askedQuestionTitle = request.form['questionTitle'] # Getting Question Title
    askedQuestionDescription = request.form['questionDescription'] # Getting Question Description
    askedQuestionCategory = request.form['selectACategory'] # Getting Category Id of the question
    
    # Checking if question is having a title and a description
    if len(askedQuestionTitle) < 0 or len(askedQuestionDescription)<0:
        print('asjs')
        flash('The Question must have a title and a description',category='error') # Flashing Error message if question is not having a title and a description
        return redirect(f'/profile/{profileUserName}') # Returning to same URL if question is not having a title or description
    else:
        newQuestion = Question(questionId=askedQuestionId,questionTitle=askedQuestionTitle,questionDescription=askedQuestionDescription,userNameOfAsker=profileUserName,realNameOfAsker=userData.realNameOfUser,categoryId=askedQuestionCategory) # Creating Instance of Question Object of Database

        try:
            db.session.add(newQuestion)
            db.session.commit()
            flash('Question Added Succesfully',category='success')
            return redirect(f'/question/{askedQuestionId}') # Redirecting to questions page

        except:
            flash('Some Error Occured while adding the question',category='error')
            return redirect(f'/profile/{profileUserName}') # Redirecting to questions page