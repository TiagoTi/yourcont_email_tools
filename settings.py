from dotenv import load_dotenv
import os
load_dotenv()


class Configuration:
    default_email = os.getenv('DEFAULT_EMAIL', 'test@email.com')
    MAILGUN_API_URL = os.getenv('MAILGUN_API_URL')
    YOURCOUNT_EMAIL_FROM = os.getenv('YOURCOUNT_EMAIL_FROM')
    MAILGUN_API_AUTH = os.getenv('MAILGUN_API_AUTH')
