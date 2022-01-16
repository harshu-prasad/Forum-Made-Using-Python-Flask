from flask import Blueprint,request,redirect,flash
from .models import Answer
from . import db # Importing Database Variable
import uuid
from flask_login import current_user # Importing current_user from flask_login to get information about logged in user

answerQuestion = Blueprint('answerQuestion',__name__,template_folder='templates') # Creating Blueprint to adress /answerQuestion endpoint

@answerQuestion.route('/<string:questionId>',methods=['POST'])
def answerQuestionFunction(questionId):
    answerId = uuid.uuid4().hex # Generating random ids for answers of questions
    answerDescription = request.form['answerOfQuestion'] # Getting Answer of the Question
    userNameOfAnswerer = current_user.userName # Getting userName of Current User
    realNameOfAnswerer = current_user.realNameOfUser # Getting Real Name of Current User

    if len(answerDescription) < 10:
        flash('The answer is too short, Please try to put atleast 10 characters', category='error')
        return redirect(f'/question/{questionId}') # Redirecting to the question Page
    else:
        answerObject = Answer(answerId=answerId,questionIdOfAnswer=questionId,answerDescription=answerDescription,userNameOfAnswerer=userNameOfAnswerer,realNameOfAnswerer=realNameOfAnswerer) # Creating Answer Object for Database

        try:
            db.session.add(answerObject) # Adding answer to the database
            db.session.commit() # Commitin Database
            flash('Successfully Answered the Question', category='success')
            return redirect(f'/question/{questionId}') # Redirecting to the question Page
        except:
            flash('Some Error Occured, Your answer might not have been added', category='error')
            return redirect(f'/question/{questionId}') # Redirecting to the question Page