from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # Initializing Flask Module
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # ADD This line to remove warnings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# Make '/' route and rendering home.html page on this route
@app.route('/')
def renderHomePageFunction():
    return render_template('home.html') # Rendering HTML Page

# Make '/category/categoryId' route and rendering category.html page with specific data according to Id
@app.route('/category/<string:categoryId>')
def renderCategoryPageFunction(categoryId):
    return render_template('category.html') # Rendering HTML Page

# Make '/question/questionId' route and rendering question.html page with specific data according to Id
@app.route('/question/<string:questionId>')
def renderQuestionPageFunction(questionId):
    return render_template('question.html') # Rendering HTML Page

# Make '/category/categoryId' route and rendering profile.html page with specific data according to Id
@app.route('/profile/<string:profileId>')
def renderProfilePageFunction(profileId):
    return render_template('profile.html') # Rendering HTML Page

if __name__ == '__main__':
    app.run(debug=True) # Runs Server at port 5000