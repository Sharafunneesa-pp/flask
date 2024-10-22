from flask import Flask,render_template
# initialise 
"""
it will create an instance of the flask class.
which will be your WSGI(Web server gateway interface) application.
"""
#WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Wecome to flask learning</h1></html>"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


# this is the entry point of any .py file
if __name__=="__main__":
    app.run(debug=True) # entire flask going to run

 # ths is how jinga2 engine working   