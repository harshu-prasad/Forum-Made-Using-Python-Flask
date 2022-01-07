from flask import Blueprint,render_template # Importing Blueprint to handle routes related to category pages

home = Blueprint('home',__name__,template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

# Rendering home.html page for '/' route
@home.route('/')
def renderHomePage():
    return render_template('home.html') # Rendering HTML Page