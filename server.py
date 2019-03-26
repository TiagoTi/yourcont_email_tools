import os
import sqlite3
from flask import Flask, render_template, request, redirect, g, url_for, flash
from settings import ADDRESS_WEB, PORT_WEB
from models.email_contract import ContractEmail
from models.email_welcome import WelcomeEmail
from models.email_meeting import MeetingSolicitationEmail
from models.email_call import CallEmail
from models.email_routine_docs_email import RoutineDocsEmail
from models.front_emails import cards_email
from settings import DATABASE, SECRET_KEY

app = Flask(__name__)
app.config.update(
    dict(
        DATABASE=os.path.join(app.root_path, DATABASE),
        SECRET_KEY=SECRET_KEY
    )
)

#cards
cards_email = cards_email()


@app.route('/')
def home():
    """
    This route is the initial from YourCount Email Tools.
    Render the *index.html*.
    Must be protected by authentication;
    """
    return render_template(
        'index.html',
        cards_email=cards_email
    )


@app.route('/greeting', methods=['GET', 'POST'])
def greeting():
    """
    The greeting email is send by website.
    """
    if request.method == 'POST':
        return redirect('/')
    else:
        return render_template('greeting.html')


@app.route('/welcome_to_your_cont', methods=['GET', 'POST'])
def welcome_to_your_cont():
    """
    The second email
    this route exits to tell to costumer about us feeling.
    """
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
        files_names = request.form.getlist('files_names')
        ContractEmail(
            to=request.form['email'],
            to_name=request.form['name'],
            files_names=files_names
        ).send()
        return redirect('/')
    else:
        files_names = []
        i = 0
        for item in os.listdir('./static/docs'):
            files_names.append(
                {
                    'id': f'file_{i}',
                    'text': f'{item}'.title(),
                    'value': f'{item}',
                }
            )
            i += 1

        return render_template(
            'contact_for_contract_data.html',
            files_names=files_names
        )


@app.route('/meeting_solicitation_email', methods=['GET', 'POST'])
def meeting_solicitation_email():
    """Meeting Solicitation Routes.

    GET -> render a template for type email
    POST -> send email to costumer.
    """
    if request.method == 'POST':
        email = MeetingSolicitationEmail(
            to=request.form['email'],
            to_name=request.form['name'],
            date=request.form['date'],
            hour1=request.form['hour1'],
            hour2=request.form['hour2']
        )

        email.send()
        if email.did_send:
            return redirect('/')
        else:
            return render_template('meeting_solicitation_email_error.html')
    else:
        return render_template('meeting_solicitation_email.html')


@app.route('/call_email', methods=['GET', 'POST'])
def call_email():
    """Call Routes.

    GET -> render a template for type email
    POST -> send email to costumer.
    """
    if request.method == 'POST':
        email = CallEmail(
            to=request.form['email'],
            to_name=request.form['name'],
            date=request.form['date'],
            hour1=request.form['hour1'],
            link=request.form['link']
        )

        email.send()
        if email.did_send:
            return redirect('/')
        else:
            return render_template('call_email_error.html')
    else:
        return render_template('call_email.html')


@app.route('/routine_docs', methods=['GET', 'POST'])
def routine_docs():
    if request.method == 'POST':
        files_names = request.form.getlist('files_names')
        RoutineDocsEmail(
            to=request.form['email'],
            to_name=request.form['name'],
            files_names=files_names
        ).send()
        return redirect('/')
    else:
        files_names = []
        i = 0
        for item in os.listdir('./static/docs'):
            files_names.append(
                {
                    'id': f'file_{i}',
                    'text': f'{item}'.title(),
                    'value': f'{item}',
                }
            )
            i += 1

        return render_template(
            'routine_docs.html',
            files_names=files_names
        )


@app.route('/customer', methods=['GET', 'POST'])
def customer():
    if request.method == 'POST':
        db = get_db()
        db.execute(
            'insert into customer (name, email) values (?, ?)',
            [request.form['name'], request.form['email']]
        )
        db.commit()
        flash('New entry was successfully posted')
        return redirect(url_for('customer'))
    else:
        db = get_db()
        cur = db.execute('select id, name, email from customer order by id desc')
        customers = cur.fetchall()
        return render_template('customer.html', customers=customers)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


def init_db():
    """Clear existing data and create new tables."""
    db = get_db()

    with app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


if __name__ == "__main__":
    app.run(host=ADDRESS_WEB, port=PORT_WEB, debug=True)
