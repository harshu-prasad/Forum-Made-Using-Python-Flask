''' PROJECT NAME : Pinnacle Forum '''
''' DESCRIPTION : This is a forum made using Python Flask for backend. For the Frontend Bootstrap has been extensively used with HTML, CSS and Javascript '''
''' AUTHOR : Harshu Prasad Shukla '''


""" FILE DESCRIPTION : THIS IS THE MAIN FILE OF THE PROJECT THAT WILL RUN THE WEBSITE """

from views import createApp # Importing createApp from __init__.py file in views directory
import os

app = createApp() # Creating app using function createApp from __init__.py file in views directory

if __name__ == '__main__':
    app.run() # Runs Server at port 5000
    # app.run(host='0.0.0.0',debug=False,port=int(os.environ.get("PORT", 5000))) # Runs Server at port 5000