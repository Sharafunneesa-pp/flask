from flask import Flask,render_template,request
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

@app.route("/index",methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f"hello {name}!"
    return render_template("form.html")



# this is the entry point of any .py file
if __name__=="__main__":
    app.run(debug=True) # entire flask going to run

