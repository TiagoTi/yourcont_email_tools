from models.email_contract import ContractEmail
from models.execptions import EmailWithoutAttachmentsException
import pytest


@pytest.fixture()
def attachments():
    return [
        'contract_antares.txt',
        'contract_antares_complemento.txt'
    ]


@pytest.fixture()
def contract():
    attachments = [
        'contract_antares.txt',
        'contract_antares_complemento.txt'
    ]
    return ContractEmail(to='tester@test.py', to_name='Tester', files_names=attachments)


@pytest.fixture()
def images():
    return [
        'logo_slim.png',
        'main_picture_contract.png',
        'footer_icon_facebook.png',
        'footer_icon_instagram.png'
    ]


def test_contract_email_payload(contract):
    assert contract.to_payload['to'] == 'Tester <tester@test.py>'
    assert contract.to_payload['from'] == 'no-replay@yourcont.com'
    assert contract.to_payload['subject'] == 'Your Cont, contratos para: Tester!'


def test_contract_email_images(contract, images):
    for i in contract.images:
        assert i in images


def test_contract_email_attachement(contract):
    assert contract.attachements


def test_contract_email_templates(contract, images):
    phrase = 'Agora que você já escolheu a Yourcont como sua parceira'
    assert phrase in contract.to_payload['text']
    assert phrase in contract.to_payload['html']

    for i in images:
        assert i in contract.to_payload['html']


def test_contract_email_templates_read_deploy(contract):
    assert '<!--' not in contract.to_payload['html']
    assert '-->' not in contract.to_payload['html']
    assert '../../static/email/img/' not in contract.to_payload['html']


def test_contract_email_attachments(contract, attachments):
    for a in contract.attachements:
        assert a in attachments


def test_dont_have_contratc_email_without_attachemnts():
    with pytest.raises(EmailWithoutAttachmentsException):
        ContractEmail(to='tester@test.py', to_name='Tester')
