from api.auth import AuthAPI  # import auth helper used to retrieve authentication tokens


def test_get_token():  # pytest test function that validates the auth token helper

    token = AuthAPI.get_token()  # call static method to retrieve a token

    print(token)  # print token for debug visibility during test execution
    

    assert token is not None  # assert that the helper returns a non-null token