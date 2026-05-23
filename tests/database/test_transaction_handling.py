from database.db_manager import (
    DBManager
)


def test_transaction_rollback():

    db = DBManager()

    db.create_users_table()

    db.delete_user(
            "TransactionUser"
        )

    db.commit_transaction()

    try:

        db.begin_transaction()

        db.insert_user(

            "TransactionUser",

            "QA"
        )

        raise Exception(
            "Simulated Failure"
        )

        db.commit_transaction()

    except Exception as e:

        print(
            f"Error occurred: {e}"
        )

        db.rollback_transaction()

    user = db.fetch_user_by_name(
        "TransactionUser"
    )

    print(user)

    assert user is None

    db.close_connection()