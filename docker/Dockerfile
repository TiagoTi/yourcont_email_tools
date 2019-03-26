FROM python:3.6
COPY requirements.txt /tmp
RUN apt update -y && apt install -y sqlite3
RUN pip install -r /tmp/requirements.txt