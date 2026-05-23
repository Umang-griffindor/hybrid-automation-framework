from api.api_client import APIClient

from api.api_headers import APIHeaders

from database.db_manager import (
    DBManager
)


def test_api_db_validation():

    api_client = APIClient()

    db = DBManager()

    db.create_users_table()

    payload = {

        "name": "IntegratedUser",

        "job": "SDET"
    }

    response, response_time = (

        api_client.post(

            "https://reqres.in/api/users",

            payload=payload,

            headers=
            APIHeaders.default_headers()
        )
    )

    response_data = (
        response.json()
    )

    api_user_name = (
        response_data.get("name")
    )

    assert (
        api_user_name
        == payload["name"]
    )

    print(
        f"API Response: "
        f"{response_data}"
    )

    assert (
        response.status_code
        == 201
    )

    db.insert_user(

        payload["name"],

        payload["job"]
    )

    db_user = (
        db.fetch_user_by_name(
            payload["name"]
        )
    )

    print(
        f"DB User: "
        f"{db_user}"
    )

    assert db_user is not None

    assert (
        db_user[1]
        == payload["name"]
    )

    assert (
        db_user[2]
        == payload["job"]
    )

    db.close_connection()