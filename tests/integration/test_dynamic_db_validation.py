from api.api_client import APIClient

from api.api_headers import APIHeaders

from database.db_manager import (
    DBManager
)


def test_dynamic_db_validation():

    api_client = APIClient()

    db = DBManager()

    db.create_users_table()

    payload = {

        "name": "DynamicUser",

        "job": "Architect"
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

    db.commit_transaction()

    inserted_user = (
        db.fetch_user_by_name(
            payload["name"]
        )
    )

    dynamic_user_id = (
        inserted_user[0]
    )

    print(
        f"Dynamic User ID: "
        f"{dynamic_user_id}"
    )

    db_user = db.fetch_user_by_id(
        dynamic_user_id
    )

    print(
        f"Fetched User: "
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