from api.api_client import APIClient

from api.api_headers import APIHeaders


def test_request_chaining():

    api_client = APIClient()

    headers = (
        APIHeaders.default_headers()
    )

    create_payload = {

        "name": "Umang",

        "job": "Automation Engineer"
    }

    create_response = api_client.post(

        "https://reqres.in/api/users",

        payload=create_payload,

        headers=headers
    )

    create_data = (
        create_response.json()
    )

    print(
        f"Create Response: "
        f"{create_data}"
    )

    user_id = create_data.get(
        "id"
    )

    print(
        f"Generated User ID: "
        f"{user_id}"
    )

    assert user_id is not None

    update_payload = {

        "name": "Umang Updated",

        "job": "Senior Engineer"
    }

    update_response = api_client.put(

        f"https://reqres.in/api/users/{user_id}",

        payload=update_payload,

        headers=headers
    )

    print(
        f"Update Response: "
        f"{update_response.json()}"
    )

    assert (
        update_response.status_code
        == 200
    )

    delete_response = api_client.delete(

        f"https://reqres.in/api/users/{user_id}",

        headers=headers
    )

    print(
        f"Delete Status: "
        f"{delete_response.status_code}"
    )

    assert (
        delete_response.status_code
        == 204
    )