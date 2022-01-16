''' FILE DESCRIPTION :- THIS FILE WILL HANDLE THE `/deleteQuestion` ENDPOINT WHICH WILL HELP THE WEBSITE TO DELETE QUESTIONS ASKED BY USER '''

from flask import Blueprint,flash,redirect # Importing Blueprint to handle routes related to requests of the login of the website
from .models import Question # Importing `Question` class from models.py to handle deleting of Questions
from . import db # Importing db from __init__.py to push changes in database
from flask_login import current_user,login_required # Importing current_use/r and login_required to get information about curret user and checking if user has logged in before running deleteQuestionFunction

deleteQuestion = Blueprint('deleteQuestion',__name__,template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

# Handling requests related deleting questions for specific question ID's
@deleteQuestion.route('/<string:questionId>')
@login_required
def deleteQuestionFunction(questionId):
    questionElement = Question.query.filter_by(questionId=questionId).first() # Getting the Question havng specific Id which's in URL

    try:
        db.session.delete(questionElement)
        db.session.commit()
        flash('Successfully deleted Question',category='success')
        return redirect(f'/profile/{current_user.userName}')
    except:
        flash('Some Error Occured, your question might not have deleted',category='error')
        return redirect(f'/profile/{current_user.userName}')