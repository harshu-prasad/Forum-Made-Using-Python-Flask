from flask import Blueprint,render_template # Importing Blueprint to handle routes related to category pages

category = Blueprint('category',__name__,template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

# Make '/categoryId' route and rendering category.html page with specific data according to Id
@category.route('/<string:categoryId>')
def renderCategoryPageFunction(categoryId):
    print('Everything Worked perfectly till here')
    return render_template('category.html') # Rendering HTML Page