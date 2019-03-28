import requests
from settings import Configuration
import pdb


def send(data, file_names, attached_filename):
    files = []
    for file_name in file_names:
        files.append(("inline", open("static/email/img/{}".format(file_name), 'rb')))

    if attached_filename:
        for attachment in attached_filename:
            files.append(("attachment", open("static/docs/{}".format(attachment), 'rb')))

    print("Files : ", files)

    try:
        r = requests.post(
            Configuration.MAILGUN_API_URL,
            auth=("api", Configuration.MAILGUN_API_AUTH),
            files=files,
            data=data
        )
        return True
    except Exception as e:
        print('fail', e)

