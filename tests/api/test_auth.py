from api.auth import AuthAPI


def test_get_token():

    token = AuthAPI.get_token()

    print(token)
    

    assert token is not None