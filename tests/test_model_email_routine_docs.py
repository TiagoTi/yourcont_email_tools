from models.email_routine_docs_email import RoutineDocsEmail
from models.execptions import EmailWithoutAttachmentsException
import pytest


@pytest.fixture()
def attachments():
    return [
        'routine_docs_email.txt',
        'routine_docs_email_complement.txt'
    ]


@pytest.fixture()
def routine_docs_email():
    attachments = [
        'routine_docs_email.txt',
        'routine_docs_email_complement.txt'
    ]
    return RoutineDocsEmail(to='tester@test.py', to_name='Tester', files_names=attachments)


@pytest.fixture()
def images():
    return [
        'logo_slim.png',
        'main_picture_contract.png',
        'footer_icon_facebook.png',
        'footer_icon_instagram.png'
    ]


def test_routineDocsEmail_email_payload(routine_docs_email):
    assert routine_docs_email.to_payload['to'] == 'Tester <tester@test.py>'
    assert routine_docs_email.to_payload['from'] == 'no-replay@yourcont.com'
    assert routine_docs_email.to_payload['subject'] == 'Rotina de Documentos'


def test_routineDocsEmail_email_images(routine_docs_email, images):
    for i in routine_docs_email.images:
        assert i in images


def test_routineDocsEmail_email_attachement(routine_docs_email):
    assert routine_docs_email.attachements


def test_routineDocsEmail_email_templates(routine_docs_email, images):
    phrase = 'Rotina de Documentos'
    assert phrase in routine_docs_email.to_payload['text']
    assert phrase in routine_docs_email.to_payload['html']

    for i in images:
        assert i in routine_docs_email.to_payload['html']


def test_routineDocsEmail_email_templates_read_deploy(routine_docs_email):
    assert '<!--' not in routine_docs_email.to_payload['html']
    assert '-->' not in routine_docs_email.to_payload['html']
    assert '../../static/email/img/' not in routine_docs_email.to_payload['html']


def test_routineDocsEmail_email_attachments(routine_docs_email, attachments):
    for a in routine_docs_email.attachements:
        assert a in attachments


def test_dont_have_contratc_email_without_attachemnts():
    with pytest.raises(EmailWithoutAttachmentsException):
        RoutineDocsEmail(to='tester@test.py', to_name='Tester')
