from models.email_meeting import MeetingSolicitationEmail
from models.execptions import \
    LinkIsRequired, \
    FirstHourIsRequired, \
    SeccoundHourIsRequired, \
    DateIsRequired
import pytest


@pytest.fixture()
def meeting():
    return MeetingSolicitationEmail(
        to='tester@test.py',
        to_name='Tester',
        date='01/01/20001',
        hour1='09:00',
        hour2='18:40',
        link='http://www.meeting.com.br'
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


def test_meeting_email_payload(meeting):
    assert meeting.to_payload['to'] == 'Tester <tester@test.py>'
    assert meeting.to_payload['from'] == 'no-replay@yourcont.com'
    assert meeting.to_payload['subject'] == 'A Your Cont gostaria de falar com você!'


def test_meeting_email_images(meeting, images):
    for i in meeting.images:
        assert i in images


def test_meeting_email_attachement(meeting):
    assert not meeting.attachements


def test_meeting_email_templates(meeting, images):
    phrase = 'Agora que você já concluiu duas etapas, queremos saber o melhor horário para nossa reunião por vídeo chamada.'
    assert phrase in meeting.to_payload['text']
    assert phrase in meeting.to_payload['html']

    for i in images:
        assert i in meeting.to_payload['html']


def test_meeting_email_templates_read_deploy(meeting):
    assert '<!--' not in meeting.to_payload['html']
    assert '-->' not in meeting.to_payload['html']
    assert '../../static/email/img/' not in meeting.to_payload['html']


def test_dont_have_contratc_email_without_attachemnts():
    with pytest.raises(FirstHourIsRequired):
        MeetingSolicitationEmail(to='tester@test.py', to_name='Tester', date='01/01/20001', hour2='18:40', link='http://www.meeting.com.br')
    with pytest.raises(SeccoundHourIsRequired):
        MeetingSolicitationEmail(to='tester@test.py', to_name='Tester', date='01/01/20001', hour1='09:00', link='http://www.meeting.com.br')
    with pytest.raises(DateIsRequired):
        MeetingSolicitationEmail(to='tester@test.py', to_name='Tester', hour1='09:00', hour2='18:40', link='http://www.meeting.com.br')
    with pytest.raises(LinkIsRequired):
        MeetingSolicitationEmail(to='tester@test.py', to_name='Tester', date='01/01/20001', hour1='09:00', hour2='18:40')