from flask import Blueprint,render_template # Importing Blueprint to handle routes related to category pages
from flask_login import current_user # Importing Details of Current User using flask_login
from .models import Category, Question

category = Blueprint('category',__name__,template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

# Make '/categoryId' route and rendering category.html page with specific data according to Id
@category.route('/<string:categoryId>')
def renderCategoryPageFunction(categoryId):
    categoryData = Category.query.filter_by(categoryId=categoryId).first() # Geting Data of the category having specific category id's
    questionData = Question.query.filter_by(categoryId=categoryId) # Getting the list of questions having category id same as that of the page
    areQuestionsNotThere = Question.query.filter_by(categoryId=categoryId).count() # Checking wether if there are some questions of this category or not
    if areQuestionsNotThere == 0:
        return render_template('category.html',user=current_user,category=categoryData,noQuestions=True) # Rendering HTML Page
    else:
        return render_template('category.html',user=current_user,category=categoryData,questions=questionData,noQuestions=False) # Rendering HTML Page