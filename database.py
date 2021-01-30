from _database import *


class DatabaseManager:
    def __init__(self) -> None:
        self.driver = database

    def sign_in(self, login: str, password: str) -> bool or Exception:
        cursor = database.execute_sql(
            f"SELECT * from users where users.login='{login}' and users.password='{password}';"
        )

        user = cursor.fetchone()

        if not user:
            return False

        return user

