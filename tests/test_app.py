import os
import tempfile

import pytest

import server as flaskr

@pytest.fixture
def client():
    #db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
    flaskr.app.config['TESTING'] = True
    client = flaskr.app.test_client()

    #with flaskr.app.app_context():
        #flaskr.init_db()

    yield client
    print('Fim de Jogo')
    #os.close(db_fd)
    #os.unlink(flaskr.app.config['DATABASE'])


def test_empty_db(client):
    """Start with a blank database."""

    # rv = client.get('/')
    # assert b'Escolha um email para enviar:' in rv.data
