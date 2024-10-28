#building url dynamically
#variable rule
#jinga 2 template engine- any information get from form  can passed 



### jinga2 template engine
"""
{{ }} expressions to print output in html
{% %} conditions, for loops
{#  #} comments

"""


from flask import Flask,render_template,request,redirect,url_for
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



# passing value in this  and giving restrictions
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


@app.route("/fail/<int:score>") #assigning a rule to variable
def fail(score):

    return render_template('result.html',results=score)

@app.route('/submits',methods=['POST','GET'])
def submits():
    total_score=0
    if request.method=='POST':
        science=float(request.form["science"])
        maths=float(request.form["maths"])
        total_score=(science+maths)/2
    else:
        return render_template('getresult.html')
    return redirect(url_for('successres',score=total_score)) # building dynamic url


#if condition
@app.route("/successif/<int:score>") #assigning a rule to variable
def successif(score):
    res=""

    return render_template('result.html',results=score)


# this is the entry point of any .py file
if __name__=="__main__":
    app.run(debug=True) # entire flask going to run


