''' PROJECT NAME : Pinnacle Forum '''
''' DESCRIPTION : This is a forum made using Python Flask for backend. For the Frontend Bootstrap has been extensively used with HTML, CSS and Javascript '''
''' AUTHOR : Harshu Prasad Shukla '''

""" FILE DESCRIPTION : THIS IS THE MAIN FILE OF THE PROJECT THAT WILL RUN THE WEBSITE """

from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from routes.home import home # Importing home from home.py to adress '/' route of website
from routes.category import category # Importing category from category.py file Variable to create route for category pages
from routes.question import question # Importing question from question.py file Variable to create route for question pages
from routes.profile import profile # Importing profile from profile.py file Variable to create route for profile pages
from routes.askQuestion import askQuestion # Importing askQuestion to adress `/askQuestion` endpoint

app = Flask(__name__) # Initializing Flask Module
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # ADD This line to remove warnings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mainDatabaseForForum.db'
db = SQLAlchemy(app)

app.register_blueprint(home,url_prefix="/") # Registering Blueprint for category pages so that when category pages are called then code of category pages are used

app.register_blueprint(category,url_prefix="/category") # Registering Blueprint for category pages so that when category pages are called then code of category pages are used

app.register_blueprint(question,url_prefix="/question") # Registering Blueprint for question pages so that when question pages are called then code of question pages are used

app.register_blueprint(profile,url_prefix="/profile") # Registering Blueprint for profile pages so that when profile pages are called then code of profile pages are used

app.register_blueprint(askQuestion,url_prefix="/askQuestion") # Registering askQuestion Endpoint in blueprint

if __name__ == '__main__':
    app.run(debug=True) # Runs Server at port 5000