
from models.emails import Email, WelcomeEmail
from util.tools import helper_load_template


def test_basic():
    text = 'Congratulations Tiago, you just sent an email with Mailgun!  You are truly awesome!'
    html = '<h1>oi</h1>'

    email = Email(to_name='Destinatary', to='destinaratio@email.com', text=text, html=html)

    expected_payload = {
        "from": "test@email.com",
        "to": "Destinatary <destinaratio@email.com>",
        "subject": "Your Cont",
        "text": text,
        "html": html
    }
    assert email.to_payload == expected_payload


def test_welcome():

    email = WelcomeEmail(to_name='Destinatary', to='destinaratio@email.com')
    assert email.subject == "Your Cont Destinatary!"
    assert email.to_text() == helper_load_template('templates', 'email', 'welcome_to_your_cont', 'txt')\
        .format('Destinatary')
