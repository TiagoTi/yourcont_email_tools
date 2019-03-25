from models.emails import Email
from models.execptions import EmailWithoutAttachmentsException

class RoutineDocsEmail(Email):

    def __init__(self, **kwargs):
        kwargs['text'] = self.template('txt', kwargs['to_name'], 'routine_docs_email')
        kwargs['html'] = self.template('html', kwargs['to_name'], 'routine_docs_email')
        super(RoutineDocsEmail, self).__init__(**kwargs)
        self._subject = 'Rotina de Documentos'.format(kwargs['to_name'])
        self._files_names_images = ['main_picture_contract.png', 'logo_slim.png', 'footer_icon_facebook.png', 'footer_icon_instagram.png']
        try:
            if len(kwargs['files_names']) > 0:
                self._files_attachement = kwargs['files_names']
            else:
                raise EmailWithoutAttachmentsException('Não existe email de contrato sem anexo')
        except:
            raise EmailWithoutAttachmentsException('Não existe email de contrato sem anexo')



