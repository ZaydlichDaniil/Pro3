import sqlite3
import hashlib

# Функція для хешування пароля
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Підключення до бази даних (або створення, якщо її не існує)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Створення таблиці користувачів
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    login TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    full_name TEXT NOT NULL
)
""")

# Додавання прикладового користувача
login = "DZ"
password = hash_password("secure123")  # прикладовий пароль
full_name = "Зайдліч Данііл Максимович"

try:
    cursor.execute("INSERT INTO users (login, password, full_name) VALUES (?, ?, ?)",
                   (login, password, full_name))
    print("Користувача успішно додано.")
except sqlite3.IntegrityError:
    print("Користувач із таким логіном вже існує.")

# Збереження змін і закриття з'єднання
conn.commit()
conn.close()