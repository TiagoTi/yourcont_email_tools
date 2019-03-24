from models.emails import Email
from models.execptions import EmailWithoutAttachmentsException

class ContractEmail(Email):

    def __init__(self, **kwargs):
        kwargs['text'] = self.template('txt', kwargs['to_name'], 'contact_for_contract_data')
        kwargs['html'] = self.template('html', kwargs['to_name'], 'contact_for_contract_data')
        super(ContractEmail, self).__init__(**kwargs)
        self._subject = 'Your Cont, contratos para: {}!'.format(kwargs['to_name'])
        self._files_names_images = ['main_picture_contract.png', 'logo_slim.png', 'footer_icon_facebook.png', 'footer_icon_instagram.png']
        try:
            self._files_attachement = kwargs['files_names']
        except:
            raise EmailWithoutAttachmentsException('Não existe email de contrato sem anexo')



