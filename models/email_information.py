from models.emails import Email


class InformationEmail(Email):

    def __init__(self, **kwargs):
        kwargs['text'] = self.template('txt', kwargs['to_name'], 'rotine_info_to_your_cont')
        kwargs['html'] = self.template('html', kwargs['to_name'], 'rotine_info_to_your_cont')
        super(InformationEmail, self).__init__(**kwargs)
        self._subject = 'Rotina de informações!'
        self._files_names_images = [
            'main_picture_information.jpg', 'logo_slim.png',
            'footer_icon_facebook.png', 'footer_icon_instagram.png'
        ]
