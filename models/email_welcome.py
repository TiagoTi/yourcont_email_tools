from models.emails import Email


class WelcomeEmail(Email):

    def __init__(self, **kwargs):
        kwargs['text'] = self.template('txt', kwargs['to_name'], 'welcome_to_your_cont')
        kwargs['html'] = self.template('html', kwargs['to_name'], 'welcome_to_your_cont')
        super(WelcomeEmail, self).__init__(**kwargs)
        self._subject = 'Bem vindo ao Your Cont {}!'.format(kwargs['to_name'])
        self._files_names_images = [
            'main_picture_welcome.jpg', 'logo_slim.png',
            'footer_icon_facebook.png', 'footer_icon_instagram.png'
        ]
