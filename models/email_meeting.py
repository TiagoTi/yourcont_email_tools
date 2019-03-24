from models.emails import Email
from models.execptions import \
    LinkIsRequired, \
    FirstHourIsRequired, \
    SeccoundHourIsRequired, \
    DateIsRequired
from util.tools import helper_load_template as load_tmp

class MeetingSolicitationEmail(Email):

    def __init__(self, **kwargs):
        self._create_meeting(kwargs)

        kwargs['text'] = MeetingSolicitationEmail.template('txt', kwargs['to_name'], 'meeting_solicitation_email', meeting=self._meeting)
        kwargs['html'] = MeetingSolicitationEmail.template('html', kwargs['to_name'], 'meeting_solicitation_email', meeting=self._meeting)

        super(MeetingSolicitationEmail, self).__init__(**kwargs)
        self._subject = 'A Your Cont gostaria de falar com você!'
        self._files_names_images = [
            'main_picture_meeting.png', 'logo_slim.png',
            'footer_icon_facebook.png', 'footer_icon_instagram.png'
        ]

    @staticmethod
    def template(ext, name, template_name, **kwargs):
        return load_tmp(
            'templates',
            'email',
            template_name, ext
        ).format(name, **kwargs['meeting'])


    def _create_meeting(self, meeting):
        self._meeting = {}

        if 'date' in meeting:
            self._meeting['date'] = meeting['date']
        else:
            raise DateIsRequired('Data para runião é obrigatório')

        if 'hour1' in meeting:
            self._meeting['hour1'] = meeting['hour1']
        else:
            raise FirstHourIsRequired('Primeira opção de hora para runião é obrigatório')

        if 'hour2' in meeting:
            self._meeting['hour2'] = meeting['hour2']
        else:
            raise SeccoundHourIsRequired('Segunda opção de hora para runião é obrigatório')

        if 'link' in meeting:
            self._meeting['link'] = meeting['link']
        else:
            raise LinkIsRequired('link para runião é obrigatório')

        self._meeting = {
            'date': meeting['date'] ,
            'hour1': meeting['hour1'],
            'hour2': meeting['hour2'],
            'link': meeting['link']
        }
