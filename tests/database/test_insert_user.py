from database.db_manager import (
    DBManager
)


def test_insert_user():

    db = DBManager()

    db.create_users_table()

    db.insert_user(

        "Umang",

        "Automation Engineer"
    )

    user = db.fetch_user_by_name(
        "Umang"
    )

    print(user)

    assert user is not None

    assert user[1] == "Umang"

    assert (
        user[2]
        == "Automation Engineer"
    )