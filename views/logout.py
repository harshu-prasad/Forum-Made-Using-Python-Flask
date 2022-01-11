from flask import Blueprint,flash,redirect # Importing Blueprint to handle routes related to requests to logout a user
from flask_login import login_required,logout_user # Importing Modules to logout the user

logout = Blueprint('logout',__name__,template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@logout.route('/')
@login_required
def logoutUser():
    logout_user() # Logging User Out
    flash("Logged Out Successfully",category='success')
    return redirect('/')