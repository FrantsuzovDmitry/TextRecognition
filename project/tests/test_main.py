import pytest
from project.main import app
import os

basedir = os.path.abspath(os.path.dirname(__file__))


@pytest.fixture()
def client():
    return app.test_client()


def send_post(client, data: dict, url: str = '/'):
    response = client.post(
        url,
        data=data,
    )
    return response


def test_true_200(client):
    fp = open(os.path.join(basedir, 'eng.jpg'), 'rb')
    data: dict = {'file': fp}
    assert send_post(client, data).status_code == 200


if __name__ == '__main__':
    pytest.main()
