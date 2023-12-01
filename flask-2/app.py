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
    amount = request.form['amount']
    
    try:
       amount = int(request.form['amount'])
    except ValueError as exc:
       
        err = str(exc)
        if amount in err:
            flash(f"{amount} is not a valid amount")
            return redirect("/home")
    
    if from_currency.upper() not in curr_convert.curr_list:
        flash(f"{from_currency} is not valid")
        return redirect("/home")
    if to_currency.upper() not in curr_convert.curr_list:
        flash(f"{to_currency} is not valid")
        return redirect("/home")

    convert = curr_convert.convert_curr(from_currency.upper(), to_currency.upper(), amount)    
    currency_symbol = curr_convert.generate_symbol(to_currency)
    try:
        return render_template('successful.html', converted = str(convert), 
                           base_to = to_currency, symbol=currency_symbol)
    except TypeError:
        flash("please insert a currency code")
        return redirect("/home")


