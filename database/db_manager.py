import sqlite3


class DBManager:

    def __init__(self):

        self.connection = sqlite3.connect(

            "database/framework.db",

            isolation_level=None
        )

        self.cursor = (
            self.connection.cursor()
        )

    def create_users_table(self):

        query = """

            CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY,

            name TEXT,

            role TEXT
        )
        """

        self.cursor.execute(query)
   

    def insert_user(
        self,
        name,
        role
    ):

        query = """

            INSERT INTO users
            (name, role)

            VALUES (?, ?)
        """

        self.cursor.execute(

            query,

            (name, role)
        )

     

    def fetch_user_by_name(
        self,
        name
    ):

        query = """

            SELECT *
            FROM users

            WHERE name = ?
        """

        self.cursor.execute(

            query,

            (name,)
        )

        return self.cursor.fetchone()
    
    def update_user_role(
        self,
        name,
        new_role
    ):

        query = """

            UPDATE users

            SET role = ?

        WHERE name = ?
        """

        self.cursor.execute(

            query,

            (new_role, name)
        )

        

    def delete_user(
        self,
        name
    ):

        query = """

            DELETE FROM users

            WHERE name = ?
        """

        self.cursor.execute(

            query,

            (name,)
        )


    def close_connection(self):

        self.connection.close()

    def begin_transaction(self):

        self.connection.execute(
            "BEGIN"
    )


    def rollback_transaction(self):

        self.connection.rollback()


    def commit_transaction(self):

        self.connection.commit()

    def fetch_user_by_id(
        self,
        user_id
    ):

        query = """

        SELECT *
        FROM users

        WHERE id = ?
        """

        self.cursor.execute(

            query,

            (user_id,)
        )

        return self.cursor.fetchone()