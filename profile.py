from flask import Blueprint,render_template # Importing Blueprint to handle routes related to profile pages

profile = Blueprint('profile',__name__,template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

# Make '/profileId' route and rendering profile.html page with specific data according to Id
@profile.route('/<string:profileId>')
def profilePageFunction(profileId):
    return render_template('profile.html') # Rendering HTML Page