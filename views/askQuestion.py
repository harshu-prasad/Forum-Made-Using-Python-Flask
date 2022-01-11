from flask import Blueprint,render_template,request
# from flask.typing import StatusCode

askQuestion = Blueprint('askQuestion',__name__,template_folder='templates') # Creating Blueprint to adress /askQuestion endpoint

@askQuestion.route('/<string:userName>',methods=['POST'])
def askQuestionFunction():
    return render_template('home.html')