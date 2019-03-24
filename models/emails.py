from settings import Configuration
from util.tools import helper_load_template as load_tmp
from services.mailgun import send as send_mailgin_email


class Email:

    def __init__(self, **kwargs):
        self._from = kwargs['from'] if hasattr(kwargs, 'from') else Configuration.default_email
        self._to = kwargs['to']
        self._to_name = kwargs['to_name']
        self._subject = kwargs['subject'] if hasattr(kwargs, 'subject') else 'Your Cont'
        self._text = kwargs['text']
        self._html = kwargs['html']
        self._files_names_images = []
        self._files_attachement = []
        self._did_send = False

    @property
    def subject(self):
        return self._subject

    @property
    def did_send(self):
        return self._did_send

    @property
    def to_payload(self):
        return {
            'to': "{0} <{1}>".format(self._to_name, self._to),
            'from': self._from,
            'subject': self._subject,
            'text': self._text,
            'html': self._html,
        }

    @property
    def images(self):
        return self._files_names_images

    @property
    def attachements(self):
        return self._files_attachement

    def send(self):
        self._did_send = send_mailgin_email(
            self.to_payload,
            self._files_names_images,
            self._files_attachement
        )

    @staticmethod
    def template(ext, name, template_name, **kwargs):
        return load_tmp(
            'templates',
            'email',
            template_name, ext).format(name, **kwargs)

    def to_html(self):
        return self._html

    def to_text(self):
        return self._text







