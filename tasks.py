import time
from settings import RABBITMQ_DEFAULT_USER, RABBITMQ_DEFAULT_HOST
from celery import Celery
from models.emails import ContractEmail

app = Celery('tasks', broker=f'pyamqp://{RABBITMQ_DEFAULT_USER}@{RABBITMQ_DEFAULT_HOST}//')


@app.task
def add(x, y):
    t = 5
    r = x + y
    time.sleep(t)
    print("waiting x")
    time.sleep(t)
    print("waiting Y")
    time.sleep(t)
    print(f"executed {r}")
    return r


@app.task
def contract_email_task(**kwargs):
    print("Aguardando ...")
    time.sleep(5)
    print("Disparando Email ...")
    contact_for_contract_data_email = ContractEmail(
        to=kwargs['to'],
        to_name=kwargs['to_name'],
        files_names=kwargs['files_names']
    )
    contact_for_contract_data_email.send()
