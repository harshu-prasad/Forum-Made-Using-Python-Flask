from flask import Blueprint,render_template,request

askQuestion = Blueprint('askQuestion',__name__,template_folder='templates') # Creating Blueprint to adress /askQuestion endpoint

@askQuestion.route('/',methods=['POST'])
def askQuestionFunction():
    print(f"{request.form['questionTitle']} {request.form['questionContentTextArea']} {request.form['selectACategory']}")
    return render_template('profile.html')