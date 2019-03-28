import os
import tempfile
import pytest
import server
from models.email_information import InformationEmail
import mock
from mock import Mock
from mock import patch
from services import mailgun

@pytest.fixture()
def information():
    return InformationEmail(to='tester@test.py', to_name='Tester')


@pytest.fixture()
def images():
    return [
        'logo_slim.png',
        'main_picture_information.jpg',
        'footer_icon_facebook.png',
        'footer_icon_instagram.png'
    ]


@pytest.fixture
def client():
    db_fd, server.app.config['DATABASE'] = tempfile.mkstemp()
    server.app.config['TESTING'] = True
    client = server.app.test_client()

    with server.app.app_context():
        server.init_db()

    yield client
    os.close(db_fd)
    os.unlink(server.app.config['DATABASE'])


def test_information_email_payload(information):
    assert information.to_payload['to'] == 'Tester <tester@test.py>'
    assert information.to_payload['from'] == 'no-replay@yourcont.com'
    assert information.to_payload['subject'] == 'Rotina de informações!'


def test_information_email_images(information, images):
    for i in information.images:
        assert i in images


def test_information_email_attachement(information):
    assert not information.attachements


def test_informatiom_email_templates(information, images):
    phrase = 'Rotina de informações'
    assert phrase in information.to_payload['text']
    assert phrase in information.to_payload['html']

    for i in images:
        assert i in information.to_payload['html']


def test_information_email_templates_read_deploy(information):
    assert '<!--' not in information.to_payload['html']
    assert '-->' not in information.to_payload['html']
    assert '../../static/email/img/' not in information.to_payload['html']


@patch('requests.post')
def test_information_email_send(mock_return):
    mock_return.return_value = 200
    e = InformationEmail(to='test@tester.com', to_name='Tester')
    e.send()
    assert e.did_send is True


def test_shout_exist_get_for_information(client):
    html = client.get('/routine_infos').data

    assert b'form form action="routine_infos" method="post"' in html
    assert b'input type="text" id="name" name="name"' in html
    assert b'input type="email" id="email" name="email"' in html
    assert b'button type="submit"' in html


@patch('requests.post')
def test_shoud_exist_post_for_information(mock_response, client):
    mock_response.return_value = 200
    html = client.post(
        '/routine_infos',
        data=dict(
            name='Test User',
            email='user@test.com'
        ),
        follow_redirects=True
    ).data

    flash = b'Email enviado com sucesso para: Test User &lt;user@test.com&gt;'

    print(html)
    assert flash in html


def test_must_exist_dashboard_link(client):
    response = client.get('/')
    image = b'src="/static/img/cards/dossier.png"'
    heading = b'Rotina De Informa'
    href = b'href="/routine_infos"'

    assert image in response.data
    assert heading in response.data
    assert href in response.data



def test_front_email():
    from models.front_emails import cards_email
    assert len(cards_email()) > 0