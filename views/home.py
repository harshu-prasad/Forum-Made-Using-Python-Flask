from flask import Blueprint,render_template # Importing Blueprint to handle routes related to category pages
from flask_login import current_user # Importing Details of Current User using flask_login
from .models import Category
# from . import db
# import uuid

home = Blueprint('home',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

# Rendering home.html page for '/' route
@home.route('/')
def renderHomePage():
    # var1 = Category(categoryId=uuid.uuid4().hex,categoryName='Javascript',categoryDescription="JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS. Over 97 percent of websites use JavaScript on the client side for web page behavior, often incorporating third-party libraries",categoryImage='javascript-logo.png')
    # db.session.add(var1)
    # db.session.commit()
    # print('90908787hkjhkjhkhkh')
    # var2 = Category(categoryId=uuid.uuid4().hex,categoryName='Python',categoryDescription="Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects",categoryImage='python-logo.png')
    # db.session.add(var2)
    # db.session.commit()
    # print("1233469890hjgjhkljl")
    return render_template('home.html',user=current_user,categories=Category.query.all()) # Rendering HTML Page and sending details of current User