from database.db_manager import (
    DBManager
)


def test_transaction_commit():

    db = DBManager()

    db.create_users_table()

    db.begin_transaction()

    db.insert_user(

        "CommittedUser",

        "SDET"
    )

    db.commit_transaction()

    user = db.fetch_user_by_name(
        "CommittedUser"
    )

    print(user)

    assert user is not None

    assert (
        user[1]
        == "CommittedUser"
    )

    db.close_connection()