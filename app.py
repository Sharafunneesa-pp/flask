from flask import Flask
# initialise 
"""
it will create an instance of the flask class.
which will be your WSGI(Web server gateway interface) application.
"""
#WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this Flask Course.Keep Learning"



# this is the entry point of any .py file
if __name__=="__main__":
    app.run(debug=True) # entire flask going to run