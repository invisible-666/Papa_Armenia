import sqlite3

class SupportBotLogic:
    def __init__(self, db_path):
        self.db_path = db_path
        self.setup_database()

    def setup_database(self):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS family (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                name TEXT,
                surname TEXT,
                age TEXT,
                phone TEXT,
                pasport TEXT
            )
            ''')
            connection.commit()

    def get_family_info(self, name):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT surname, age, phone, pasport FROM family WHERE name = ?", (name,))
            result = cursor.fetchone()

            if result:
                surname, age, phone = result
                return f"Фамилия: {surname}, Возраст: {age}, Телефон: {phone}, Паспорт: {pasport}"
            else:
                return "Извините, информация не найдена."
