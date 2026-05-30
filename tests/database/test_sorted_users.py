from database.db_manager import (
    DBManager
)

def test_sorted_users():

    db = DBManager()

    users = (
        db.fetch_users_sorted_by_name()
    )

    print(users)

    assert users is not None

    db.close_connection()