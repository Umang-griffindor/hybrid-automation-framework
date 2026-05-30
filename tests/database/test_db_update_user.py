from database.db_manager import (
    DBManager
)


def test_update_user():

    db = DBManager()

    db.create_users_table()

    db.insert_user(

        "Rahul",

        "QA"
    )

    db.update_user_role(

        "Rahul",

        "SDET"
    )

    updated_user = (
        db.fetch_user_by_name(
            "Rahul"
        )
    )

    print(updated_user)

    assert (
        updated_user[2]
        == "SDET"
    )