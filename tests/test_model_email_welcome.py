from models.email_welcome import WelcomeEmail
import pytest
import mock
from mock import Mock
from mock import patch
from services import mailgun


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


@patch('requests.post')
def test_welcome_email_send(mock_return):
    mock_return.return_value = 200
    e = WelcomeEmail(to='test@tester.com', to_name='Tester')
    e.send()
    assert e.did_send is True
