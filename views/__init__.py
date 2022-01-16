''' FILE DESCRIPTION : THIS FILE WILL CONNECT DATABASE AND RUN BLUEPRINTS AND SOME IMPORTANT THINGS '''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path # Importing Path from os module to check path of database
from flask_login import LoginManager # Importing Class LoginManager to manage Login Details

db = SQLAlchemy() # Creating Database Instance
DATABASENAME = 'mainDatabaseForForum.db' # This is the name of the database that the website will be using

def createApp():
    ''' This function will create the app '''
    app = Flask(__name__) # Initializing Flask Module
    app.config['SECRET_KEY'] = 'themysticalprogrammer' # Setting up the secret key for the application
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # ADD This line to remove warnings
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASENAME}'
    db.init_app(app) # Adding App in Database

    from .home import home # Importing home from home.py to adress '/' route of website
    from .category import category # Importing category from category.py file Variable to create route for category pages
    from .question import question # Importing question from question.py file Variable to create route for question pages
    from .profile import profile # Importing profile from profile.py file Variable to create route for profile pages
    from .askQuestion import askQuestion # Importing askQuestion to adress `/askQuestion` endpoint
    from .signup import signup # Importing sigup to adress `/signup` endpoint
    from .login import login # Importing login to adress `/login` endpoint
    from .logout import logout # Importing logout to adress `/logout` endpoint
    from .deleteQuestion import deleteQuestion # Importing deleteQuestion to adress `/deleteQuestion` endpoint
    from .answerQuestion import answerQuestion # Importing answerQuestion to adress `/answerQuestion` endpoint

    app.register_blueprint(home,url_prefix="/") # Registering Blueprint for category pages so that when category pages are called then code of category pages are used

    app.register_blueprint(category,url_prefix="/category") # Registering Blueprint for category pages so that when category pages are called then code of category pages are used

    app.register_blueprint(question,url_prefix="/question") # Registering Blueprint for question pages so that when question pages are called then code of question pages are used

    app.register_blueprint(profile,url_prefix="/profile") # Registering Blueprint for profile pages so that when profile pages are called then code of profile pages are used

    app.register_blueprint(askQuestion,url_prefix="/askQuestion") # Registering askQuestion Endpoint in blueprint

    app.register_blueprint(signup,url_prefix="/signup") # Registering signup Endpoint in blueprint

    app.register_blueprint(login,url_prefix="/login") # Registering login Endpoint in blueprint

    app.register_blueprint(logout,url_prefix="/logout") # Registering logout Endpoint in blueprint

    app.register_blueprint(deleteQuestion,url_prefix="/deleteQuestion") # Registering deleteQuestion Endpoint in blueprint

    app.register_blueprint(answerQuestion,url_prefix="/answerQuestion") # Registering answerQuestion Endpoint in blueprint

    createDatabase(app) # Running createDatabase function to create database if it doesn't exists

    loginManagerVariable = LoginManager() # Initialising Login Manager
    loginManagerVariable.login_view = 'login.loginUser'
    loginManagerVariable.init_app(app)

    from .models import User # Importing User Class from models.py

    @loginManagerVariable.user_loader
    def loadUser(userName):
        return User.query.get(str(userName))

    return app # Returning Database so that it could run in main.py

def createDatabase(app):
    ''' This function will create database for the website '''
    if not path.exists('views/' + DATABASENAME): # If database doesn't exists
        db.create_all(app=app) # Creating Database
        print('Created Database!')