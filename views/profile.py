from flask import Blueprint,render_template # Importing Blueprint to handle routes related to profile pages
from flask_login import current_user # Importing Details of Current User using flask_login
from .models import User, Question, Category

profile = Blueprint('profile',__name__,template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

# Make '/profileId' route and rendering profile.html page with specific data according to Id
@profile.route('/<string:profileId>')
def profilePageFunction(profileId):
    userObject = User.query.filter_by(userName=profileId).first()
    userQuestions = Question.query.filter_by(userNameOfAsker=profileId)
    hasUserAskedQuestions = Question.query.filter_by(userNameOfAsker=profileId).count() # Counting wether the user has asked some questons
    if hasUserAskedQuestions == 0:
        return render_template('profile.html',user=current_user,profileUser=userObject,noQuestions=True,categoryData=Category.query.all()) # Rendering HTML Page
    else:
        return render_template('profile.html',user=current_user,profileUser=userObject,userQuestions=userQuestions,noQuestions=False,categoryData=Category.query.all()) # Rendering HTML Page