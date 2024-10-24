#building url dynamically
#variable rule
#jinga 2 template engine



### jinga2 template engine
"""
{{ }} expressions to print output in html
{% %} conditions, for loops
{#  #} comments

"""





from flask import Flask,render_template,request
# initialise 
"""
it will create an instance of the flask class.
which will be your WSGI(Web server gateway interface) application.
"""
#WSGI Application
app=Flask(__name__)


@app.route("/submit",methods=["GET","POST"])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f"hello {name}!"
    return render_template("form.html")

# # variable rule
# @app.route("/success/<int:score>") #assigning a rule to variable
# def success(score):
#     return f"The marks you got is {score}" # do typecasting


@app.route("/success/<int:score>") #assigning a rule to variable
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"

    return render_template('result.html',results=res)


@app.route("/successres/<int:score>") #assigning a rule to variable
def successres(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"

    res={'score':score,'res':res}
    return render_template('result1.html',results=res)


@app.route("/successif/<int:score>") #assigning a rule to variable
def successif(score):

    return render_template('result.html',results=score)


    


# this is the entry point of any .py file
if __name__=="__main__":
    app.run(debug=True) # entire flask going to run


