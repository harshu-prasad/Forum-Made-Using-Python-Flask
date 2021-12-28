from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime # Importing datetime to store date in database
from category import category # Importing category from category.py file Variable to create route for category pages
from question import question # Importing question from question.py file Variable to create route for question pages
from profile import profile # Importing profile from profile.py file Variable to create route for profile pages

app = Flask(__name__) # Initializing Flask Module
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # ADD This line to remove warnings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mainDatabaseForForum.db'
db = SQLAlchemy(app)

class Users(db.Model):
    # Adding Coloumns
    realNameOfUser = db.Column(db.Integer,primary_key=True)
    emailOfUser = db.Column(db.String(250),nullable=False)
    passwordOfUser = db.Column(db.String(550),nullable=False)

# Make '/' route and rendering home.html page on this route
@app.route('/')
def renderHomePageFunction():
    return render_template('home.html') # Rendering home.html Page

app.register_blueprint(category,url_prefix="/category") # Registering Blueprint for category pages so that when category pages are called then code of category pages are used

app.register_blueprint(question,url_prefix="/question") # Registering Blueprint for question pages so that when question pages are called then code of question pages are used

app.register_blueprint(profile,url_prefix="/profile") # Registering Blueprint for profile pages so that when profile pages are called then code of profile pages are used

if __name__ == '__main__':
    app.run(debug=True) # Runs Server at port 5000