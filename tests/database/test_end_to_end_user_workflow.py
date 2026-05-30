from api.api_client import APIClient
from api.api_headers import APIHeaders
from api.api_assertions import APIAssertions

from database.db_manager import (
    DBManager
)

def test_end_to_end_user_workflow():

    api_client = APIClient()

    db = DBManager()

    db.create_users_table()

    payload = {

        "name": "WorkflowUser",

        "job": "Automation Architect"
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

    APIAssertions.verify_status_code(
        response,
        201
    )

    APIAssertions.verify_response_time(
        response_time,
        3
    )

    db.delete_user(
        "WorkflowUser"
    )

    db.commit_transaction()

    db.insert_user(

        payload["name"],

        payload["job"]
    )

    db.commit_transaction()

    db_user = (
        db.fetch_user_by_name(
            "WorkflowUser"
        )
    )

    print(
        f"Database User: "
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

    db.delete_user(
        "WorkflowUser"
    )

    db.commit_transaction()

    cleanup_check = (
        db.fetch_user_by_name(
            "WorkflowUser"
        )
    )

    assert cleanup_check is None

    db.close_connection()