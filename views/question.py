from flask import Blueprint,render_template # Importing Blueprint to handle routes related to question pages

question = Blueprint('question',__name__,template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

# Make '/questionId' route and rendering question.html page with specific data according to Id
@question.route('/<string:questionId>')
def renderquestionPageFunction(questionId):
    return render_template('question.html') # Rendering HTML Page