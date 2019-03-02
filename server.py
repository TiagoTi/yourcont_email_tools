from flask import Flask, render_template, request, redirect
from models.emails import WelcomeEmail

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
