from database.db_manager import (
    DBManager
)


def test_delete_user():

    db = DBManager()

    db.create_users_table()

    db.insert_user(

        "DeleteUser",

        "QA"
    )

    db.delete_user(
        "DeleteUser"
    )

    deleted_user = (
        db.fetch_user_by_name(
            "DeleteUser"
        )
    )

    print(deleted_user)

    assert deleted_user is None