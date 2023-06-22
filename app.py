#import necessary methods and set up configs
from flask import Flask, request, render_template, redirect, flash, session, jsonify
from converter import Currency_Converter
from forex import rates_lst



 

app = Flask(__name__)
app.config['SECRET_KEY'] = "abc123"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False


@app.route("/")
def show_home():
    """Shows the home page and the form """

    return render_template("converter.html")


#get the values to be converted for the results
@app.route("/results", methods=["GET","POST"])
def handles_form():
    """Gets the user inputs, handles errors for invalid inputs based of the responses from the forex db"""
    try:
        res_from = request.form.get("from")
        res_to = request.form.get("to")
        res_amount = request.form.get("amount")
        msg = None
        # use the validation functions from the Currency_Converter class
        converter = Currency_Converter(res_from, res_to, res_amount)
        values = converter.get_values()
        result = converter.get_rate_result(*values)
        symbol = converter.get_symbol(res_to)
        #check if the inputs are valid
        # if converter.check_is_valid_from(res_from) != None:
        #     msg = converter.check_is_valid_from(res_from)
        #     flash(msg)
        #     return redirect("/")
        # elif converter.check_is_valid_to(res_to) != None:
        #     msg = converter.check_is_valid_to(res_to)
        #     flash(msg)
        #     return redirect("/")
        # elif converter.check_is_valid_amount(res_amount) != None:
        #     msg = converter.check_is_valid_amount(res_amount)
        #     flash(msg)
        #     return redirect("/")
        return render_template("results.html", symbol=symbol, result=result )
    except:
        flash("Please enter valid inputs")
        return redirect("/")


@app.route("/go-home")
def go_home():
    """Returns the user home"""

    return redirect("/")