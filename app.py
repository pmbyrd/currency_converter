#import necessary methods and set up configs
from flask import Flask, request, render_template, redirect, flash, session, jsonify

from flask_debugtoolbar import DebugToolbarExtension

from converter import Currency_Converter

# from forex

app = Flask(__name__)
app.config['SECRET_KEY'] = "abc123"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']
app.debug = True

toolbar = DebugToolbarExtension(app)



@app.route("/")
def show_home():
    """Shows the home page and the form """
    ("######################")
    return render_template("converter.html")

@app.route("/results")
def show_results():
    """Handles the request to show the converted results"""
    #if the convert currency was valid, render the results on this page the 
    print("#############")
    return redirect("/results")


#get the values to be converted for the results
@app.route("/results", methods=["POST"])
def handles_form():
    """Gets the user inputs, handles errors for invalid inputs based of the responses from the forex db"""
    
    #initialize the variables that will be passed into the template
    #get the inputs from the page
   
    res_from = request.form["from"]
    res_to = request.form["to"]
    res_amount = request.form["amount"]
   
    import pdb
    pdb.set_trace()


    #get the responses from forex

    #get the result and append it to the page


    #pass the variables into the template
 
    return render_template("results.html")


@app.route("/go-home")
def go_home():
    """Returns the user home"""

    #get the button so on click return home

    return redirect("/")