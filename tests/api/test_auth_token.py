from api.auth_api import AuthAPI


def test_get_token():

    token = AuthAPI.get_token()

    assert token is not None