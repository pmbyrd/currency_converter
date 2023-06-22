#import necessary methods and set up configs
from flask import Flask, request, render_template, redirect, flash, session, jsonify
from converter import Currency_Converter



 

app = Flask(__name__)
app.config['SECRET_KEY'] = "abc123"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

app.debug = True

# toolbar = DebugToolbarExtension(app)



@app.route("/")
def show_home():
    """Shows the home page and the form """

    return render_template("converter.html")

@app.route("/results")
def show_results():
    """Handles the request to show the converted results"""
    #if the convert currency is valid, render the results on this page the 
    
    return render_template("results.html")


#get the values to be converted for the results
@app.route("/results", methods=["POST"])
def handles_form():
    """Gets the user inputs, handles errors for invalid inputs based of the responses from the forex db"""
    
    #initialize the variables that will be passed into the template
    #get the inputs from the page
   
    res_from = request.form.get("from")
    res_to = request.form.get("to")
    res_amount = request.form.get("amount")
   
    converter = Currency_Converter(res_from, res_to, res_amount)

    values = converter.get_values()

    msg = converter.check_is_valid(res_from, res_to, res_amount)
    
   
    result = converter.get_rate_result(*values)
    symbol = converter.get_symbol(res_to)
                #pass the variables into the template   
    # if msg:
    #     flash(msg)
    #     return redirect("/")
    
    # else:
    return render_template("results.html", symbol=symbol, result=result )


@app.route("/go-home")
def go_home():
    """Returns the user home"""

    return redirect("/")