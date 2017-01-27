import pytest

from app import api


@pytest.fixture(scope="module")
def client():
    api.app.app_context().push()
    return api.app.test_client()


def test00_client(client):
    assert client.get("/").status_code == 200
