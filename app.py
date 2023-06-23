#import necessary methods and set up configs
from flask import Flask, request, render_template, redirect, flash, session, jsonify
from converter import Currency_Converter


app = Flask(__name__)
app.config['SECRET_KEY'] = "abc123"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False


@app.route("/")
def show_home():
    """Shows the home page and the form """

    return render_template("converter.html")

#get the values to be converted for the results
@app.route("/results", methods=["GET", "POST"])
def handles_form():
    """Gets the user inputs, handles errors for invalid inputs based on the responses from the forex db"""
    try:
        res_from = request.form.get("from")
        res_to = request.form.get("to")
        res_amount = request.form.get("amount")
        #handle if a user enters a blank input
        if res_from == "" or res_to == "" or res_amount == "":
            raise ValueError("Please enter a valid input")

        # Create an instance of Currency_Converter and perform validation
        converter = Currency_Converter(res_from, res_to, res_amount)

        # import pdb; pdb.set_trace()
        # Calculate the conversion result
        result = converter.get_rate_result(converter.from_curr, converter.to_curr, converter.amount)

        # Get the currency symbol
        symbol = converter.get_symbol(res_to)
        return render_template("results.html", symbol=symbol, result=result)
    
    except ValueError as e:
        flash(str(e))
        return redirect("/")




@app.route("/go-home")
def go_home():
    """Returns the user home"""

    return redirect("/")