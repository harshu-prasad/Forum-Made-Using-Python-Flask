from flask import Blueprint,render_template # Importing Blueprint to handle routes related to question pages
from flask_login import current_user # Importing Details of Current User using flask_login
from .models import Question,Answer # Importing Question Object from models.py to handle requests related to questions in the website

question = Blueprint('question',__name__,template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

# Make '/questionId' route and rendering question.html page with specific data according to Id
@question.route('/<string:questionId>')
def renderquestionPageFunction(questionId):
    questionObject = Question.query.filter_by(questionId=questionId).first() # Getting the question having ID passed in url
    answersListLength = Answer.query.filter_by(questionIdOfAnswer=questionId).count() # Counting no. of answers that assigned to the question
    if answersListLength == 0:
        return render_template('question.html',user=current_user,question=questionObject,noAnswers=True) # Rendering HTML Page
    else:
        answersList = Answer.query.filter_by(questionIdOfAnswer=questionId).all() # Getting List of Answers attached to this question
        return render_template('question.html',user=current_user,question=questionObject,noAnswers=False,answers=answersList) # Rendering HTML Page