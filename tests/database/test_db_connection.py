from database.db_manager import (
    DBManager
)


def test_create_table():

    db = DBManager()

    db.create_users_table()

    assert True