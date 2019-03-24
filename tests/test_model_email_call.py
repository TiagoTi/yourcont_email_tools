from models.email_call import CallEmail
from models.execptions import \
    LinkIsRequired, \
    FirstHourIsRequired, \
    DateIsRequired
import pytest


@pytest.fixture()
def call_e():
    return CallEmail(
        to='tester@test.py',
        to_name='Tester',
        date='01/01/2001',
        hour1='09:00',
        link='http://aper.com'
    )


@pytest.fixture()
def images():
    return [
        'logo_slim.png',
        'main_picture_meeting.png',
        'footer_icon_facebook.png',
        'footer_icon_instagram.png',
        'footer_icon_appear-in.png'
    ]


def test_call_email_payload(call_e):
    assert call_e.to_payload['to'] == 'Tester <tester@test.py>'
    assert call_e.to_payload['from'] == 'no-replay@yourcont.com'
    assert call_e.to_payload['subject'] == 'A Your Cont gostaria de falar com você!'


def test_call_email_images(call_e, images):
    for i in call_e.images:
        assert i in images


def test_call_email_attachement(call_e):
    assert not call_e.attachements


def test_call_email_templates(call_e, images):
    text_patchs = [
        '01/01/2001',
        '09:00',
        'http://aper.com',
        'Confirmação de call'
    ]

    for path_text in text_patchs:
        assert path_text in call_e.to_payload['text']
        assert path_text in call_e.to_payload['html']

    for i in images:
        assert i in call_e.to_payload['html']


def test_call_email_templates_read_deploy(call_e):
    assert '<!--' not in call_e.to_payload['html']
    assert '-->' not in call_e.to_payload['html']
    assert '../../static/email/img/' not in call_e.to_payload['html']


def test_dont_have_contratc_email_without_attachemnts():
    with pytest.raises(FirstHourIsRequired):
        CallEmail(to='tester@test.py', to_name='Tester', date='01/01/20001', link='http://www.call.com.br')
    with pytest.raises(LinkIsRequired):
        CallEmail(to='tester@test.py', to_name='Tester', date='01/01/20001', hour1='09:00')
    with pytest.raises(DateIsRequired):
        CallEmail(to='tester@test.py', to_name='Tester', hour1='09:00', link='http://www.call.com.br')
