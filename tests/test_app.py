import os
import tempfile
import pytest
import server


@pytest.fixture
def client():
    db_fd, server.app.config['DATABASE'] = tempfile.mkstemp()
    server.app.config['TESTING'] = True
    client = server.app.test_client()

    with server.app.app_context():
        server.init_db()

    yield client
    print('Fim de Jogo')
    os.close(db_fd)
    os.unlink(server.app.config['DATABASE'])


def test_empty_db(client):
    """Start with a blank database."""

    rv = client.get('/')
    assert b'Escolha um email para enviar:' in rv.data


def test_get_routine_docs(client):
    rv = client.get('/routine_docs')
    assert b'<h1>Rotina de Documentos</h1>' in rv.data


def test_add_customer(client):
    response = client.post(
        '/customer',
        data=dict(
            name='Test User',
            email='user@test.com'
        ),
        follow_redirects=True
    )

    assert b'<td>Test User</td>' in response.data
    assert b'<td>user@test.com</td>' in response.data
