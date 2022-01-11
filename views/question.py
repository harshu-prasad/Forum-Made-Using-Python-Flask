from flask import Blueprint,render_template # Importing Blueprint to handle routes related to question pages
from flask_login import current_user # Importing Details of Current User using flask_login

question = Blueprint('question',__name__,template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

# Make '/questionId' route and rendering question.html page with specific data according to Id
@question.route('/<string:questionId>')
def renderquestionPageFunction(questionId):
    return render_template('question.html',user=current_user) # Rendering HTML Page