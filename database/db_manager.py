import sqlite3


class DBManager:

    def __init__(self):

        self.connection = sqlite3.connect(
            "database/framework.db"
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

        self.connection.commit()   

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

        self.connection.commit() 

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

        self.connection.commit()

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

        self.connection.commit()