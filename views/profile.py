from curses import flash
from flask import Blueprint,request,render_template,flash,redirect # Importing Blueprint to handle routes related to profile pages
from flask_login import current_user # Importing Details of Current User using flask_login
from werkzeug.security import generate_password_hash # Importing module to hash password of the user
from .models import User, Question, Category
from . import db

profile = Blueprint('profile',__name__,template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

# Make '/profileId' route and rendering profile.html page with specific data according to Id
@profile.route('/<string:profileId>',methods=['GET','POST'])
def profilePageFunction(profileId):
    userObject = User.query.filter_by(userName=profileId).first()
    if request.method == 'POST':
        newNameOfUser = request.form['newRealName'] # Getting new Name of User
        newPasswordOfUser = request.form['newPassword'] # Getting New Password of User

        if len(newPasswordOfUser) < 5: # Checking if password is too short
            flash('Password is too short, Please type a little long password', category='error')
            return redirect(f'/profile/{profileId}') # Redirecting to the same profile

        else:
            newHashedPassword = generate_password_hash(newPasswordOfUser) # Adding Hashed Password to variable
            userObject.realNameOfUser = newNameOfUser
            userObject.passwordOfUser = newHashedPassword
            try:
                db.session.add(userObject)
                db.session.commit()
                flash('Profile Successfully Edited', category='success')
                return redirect(f'/profile/{profileId}') # Redirecting to the same profile
            except:
                flash('Some Error Occured while editing the profile, your profile may not have been changed', category='error')
                return redirect(f'/profile/{profileId}') # Redirecting to the same profile

    userQuestions = Question.query.filter_by(userNameOfAsker=profileId).all()
    hasUserAskedQuestions = Question.query.filter_by(userNameOfAsker=profileId).count() # Counting wether the user has asked some questons
    if hasUserAskedQuestions == 0:
        return render_template('profile.html',user=current_user,profileUser=userObject,noQuestions=True,categoryData=Category.query.all()) # Rendering HTML Page
    else:
        return render_template('profile.html',user=current_user,profileUser=userObject,userQuestions=userQuestions,noQuestions=False,categoryData=Category.query.all()) # Rendering HTML Page