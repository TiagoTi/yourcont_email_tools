
from models.email_welcome import WelcomeEmail
import pytest


@pytest.fixture()
def welcome():
    return WelcomeEmail(to='tester@test.py', to_name='Tester')


@pytest.fixture()
def images():
    return [
        'logo_slim.png',
        'main_picture_welcome.jpg',
        'footer_icon_facebook.png',
        'footer_icon_instagram.png'
    ]


def test_welcome_email_payload(welcome):
    assert welcome.to_payload['to'] == 'Tester <tester@test.py>'
    assert welcome.to_payload['from'] == 'no-replay@yourcont.com'
    assert welcome.to_payload['subject'] == 'Bem vindo ao Your Cont Tester!'


def test_welcome_email_images(welcome, images):
    for i in welcome.images:
        assert i in images


def test_welcome_email_attachement(welcome):
    assert not welcome.attachements


def test_welcome_email_templates(welcome, images):
    phrase = 'Agora você também faz parte do grupo de Sellers Yourcont que escolheram ter mais tempo para gerir o seu negócio e redefinir a maneira como você cuida da saúde da sua empresa.'
    assert phrase in welcome.to_payload['text']
    assert phrase in welcome.to_payload['html']

    for i in images:
        assert i in welcome.to_payload['html']


def test_welcome_email_templates_read_deploy(welcome):
    assert '<!--' not in welcome.to_payload['html']
    assert '-->' not in welcome.to_payload['html']
    assert '../../static/email/img/' not in welcome.to_payload['html']


    # self._to_name = kwargs['to_name']
    # self._subject = kwargs['subject'] if hasattr(kwargs, 'subject') else 'Your Cont'
    # self._text = kwargs['text']
    # self._html = kwargs['html']
    # self._files_names_images = []
    # self._files_attachement = []
#
# def test_basic():
#     text = 'Congratulations Tiago, you just sent an email with Mailgun!  You are truly awesome!'
#     html = '<h1>oi</h1>'
#
#     email = Email(to_name='Destinatary', to='destinaratio@email.com', text=text, html=html)
#
#     expected_payload = {
#         "from": "test@email.com",
#         "to": "Destinatary <destinaratio@email.com>",
#         "subject": "Your Cont",
#         "text": text,
#         "html": html
#     }
#     assert email.to_payload == expected_payload
#
#
# def test_welcome():
#
#     email = WelcomeEmail(to_name='Destinatary', to='destinaratio@email.com')
#     assert email.subject == "Your Cont Destinatary!"
#     assert email.to_text() == helper_load_template('templates', 'email', 'welcome_to_your_cont', 'txt')\
#         .format('Destinatary')
