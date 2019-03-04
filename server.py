from flask import Flask, render_template, request, redirect
from models.emails import WelcomeEmail, ContractEmail
from models.front_emails import cards_email

app = Flask(__name__)

#cards
cards_email = cards_email()

@app.route('/')
def home():
    return render_template('index.html', cards_email=cards_email)


@app.route('/welcome_to_your_cont', methods=['GET', 'POST'])
def welcome_to_your_cont():
    if request.method == 'POST':
        welcome_email = WelcomeEmail(to=request.form['email'], to_name=request.form['name'])
        welcome_email.send()
        if welcome_email.did_send:
            return redirect('/')
        else:
            return render_template('welcome_to_your_cont_error.html')
    else:
        return render_template('welcome_to_your_cont.html')


@app.route('/contact_for_contract_data', methods=['GET', 'POST'])
def contact_for_contract_data():
    if request.method == 'POST':
        contact_for_contract_data_email = ContractEmail(to=request.form['email'], to_name=request.form['name'])
        contact_for_contract_data_email.send()
        if contact_for_contract_data_email.did_send:
            return redirect('/')
        else:
            return render_template('contact_for_contract_data_error.html')
    else:
        return render_template('contact_for_contract_data.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
