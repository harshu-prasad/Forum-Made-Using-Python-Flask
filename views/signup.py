from flask import Blueprint,request,flash,redirect # Importing Blueprint to handle routes related to requests of the signup of the website
from flask_login import login_user # Importing stuff needed to login user
import re # Importing re module to check an email given by the user
import uuid # Importing built in module uuid for generating random Id's
from . import db # Importing db from main.py to add data in server
from .models import User # Importing User Database Model from models.py to create Users for the website
from werkzeug.security import generate_password_hash # Importing module to hash password of the user
# import 


signup = Blueprint('signup',__name__,template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside
# sys.path.append("..") # Adds higher directory to python modules path.

# Handling post requests of '/signup/' to create a user account and login
@signup.route('/',methods=['POST'])
def signupUser():
    realNameOfUserSignup = request.form['realNameOfUser'] # Getting Real Name Of User using signup form
    userNameSignup = uuid.uuid4().hex # Generating a random and unique username for the user
    print(userNameSignup)
    emailId = request.form['emailIdSignup'] # Getting emailId of the user from Form
    passwordOfUserSignup = request.form['passwordSignup'] # Getting Password of User from Form

    isEmailValid = checkEmail(emailId) # Checking wether the emailId given by user is valid or not

    # If email of User is correct
    if isEmailValid:
        doesEmailExists = User.query.filter_by(emailOfUser=emailId).first() # This variable will return true if email exists

        if not doesEmailExists: # If Email doesn't exists
            newUser = User(userName=userNameSignup,realNameOfUser=realNameOfUserSignup,emailOfUser=emailId,passwordOfUser=generate_password_hash(passwordOfUserSignup)) # Filling User Object with neccessary variables

            # Checking wether the following Code would run or not
            try:
                db.session.add(newUser) # Adding Users to Database
                db.session.commit() # Commiting Data to the Database
                login_user(newUser) # Logging in User who has created the account
                flash("Account Created Successfully",category='success')
                return redirect('/') # returning to home page

            except:
                flash("Some Error Occured while creating an account",category='error')
                return redirect('/') # returning to home page
        else:
            flash("This email already exists. Please Login to access your account",category='error')
            return redirect('/') # returning to home page

    else: # If user email isn't valid
        flash("Email is not Valid",category='error')
        print("Email is not Valid")
        return redirect('/') # returning to home page

def checkEmail(email):
    ''' This Function will check wether the email given by the user and return true or false according to that '''
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' # Creating Regex Varaible to create a skeleton of an ideal email so that if email given by the user is out of its domain the it will find it out

    if(re.search(regex,email)):   
        return True  # Returning True to show that email is valid
    else:   
        return False # Returning False to show that email is invalid