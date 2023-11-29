from flask import Flask, render_template, session, request, flash, redirect
from converter import CurrencyConverter, RatesNotAvailableError
app = Flask(__name__)
app.config['SECRET_KEY'] = 'sEcReT'

curr_convert = CurrencyConverter()


@app.route('/home')
def home_page():
    session['currencies'] = [curr_convert.curr_list]
    return render_template('conversion-form.html')
    

@app.route('/converted', methods=['POST'])
def converted():
    from_currency = request.form['from-curr']
    to_currency = request.form['to-curr']

    
    try:
        amount = int(request.form['amount'])
    except ValueError as exc:
        flash(f"{exc} is not a valid amount")
        return redirect("/home")
    

    try:
        convert = curr_convert.convert_curr(from_currency, to_currency, amount)
    except RatesNotAvailableError as exc:
        flash("Currency code invalid")
        return redirect("/home")
    currency_symbol = curr_convert.generate_symbol(to_currency)
    try:
        return render_template('successful.html', converted = str(convert), 
                           base_to = to_currency, symbol=currency_symbol)
    except TypeError:
        flash("please insert a currency code")
        return redirect("/home")


