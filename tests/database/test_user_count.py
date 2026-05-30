from database.db_manager import (
    DBManager
)

def test_user_count():

    db = DBManager()

    db.create_users_table()

    db.delete_user("CountUser1")
    db.delete_user("CountUser2")
    db.commit_transaction()

    db.insert_user(
        "CountUser1",
        "QA"
    )

    db.insert_user(
        "CountUser2",
        "SDET"
    )

    db.commit_transaction()

    count = db.get_user_count()

    print(
        f"Total Users: {count}"
    )

    assert count > 0

    db.close_connection()