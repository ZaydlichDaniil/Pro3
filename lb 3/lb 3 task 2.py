import sqlite3
import hashlib

# Хешування паролю
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Підключення до БД
def connect_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        login TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        full_name TEXT NOT NULL
    )
    """)
    conn.commit()
    return conn, cursor

# Додавання нового користувача
def add_user(login, password, full_name):
    conn, cursor = connect_db()
    try:
        cursor.execute("INSERT INTO users (login, password, full_name) VALUES (?, ?, ?)",
                       (login, hash_password(password), full_name))
        conn.commit()
        print(f"Користувача '{login}' додано.")
    except sqlite3.IntegrityError:
        print(f"Користувач '{login}' вже існує.")
    conn.close()

# Оновлення пароля користувача
def update_password(login, new_password):
    conn, cursor = connect_db()
    cursor.execute("UPDATE users SET password = ? WHERE login = ?",
                   (hash_password(new_password), login))
    if cursor.rowcount > 0:
        print("Пароль оновлено.")
    else:
        print("Користувача не знайдено.")
    conn.commit()
    conn.close()

# Перевірка автентифікації
def authenticate_user():
    conn, cursor = connect_db()
    login = input("Логін: ")
    password = input("Пароль: ")
    hashed = hash_password(password)

    cursor.execute("SELECT full_name FROM users WHERE login = ? AND password = ?", (login, hashed))
    user = cursor.fetchone()

    if user:
        print(f"Вхід дозволено. Вітаємо, {user[0]}!")
    else:
        print("Невірний логін або пароль.")
    conn.close()

# === Головне меню ===
def main():
    while True:
        print("\n--- Меню ---")
        print("1. Зареєструвати нового користувача")
        print("2. Увійти в систему")
        print("3. Змінити пароль")
        print("4. Вийти")

        choice = input("Оберіть опцію: ")

        if choice == "1":
            login = input("Введіть логін: ")
            password = input("Введіть пароль: ")
            full_name = input("Введіть повне ім'я: ")
            add_user(login, password, full_name)
        elif choice == "2":
            authenticate_user()
        elif choice == "3":
            login = input("Введіть логін: ")
            new_password = input("Введіть новий пароль: ")
            update_password(login, new_password)
        elif choice == "4":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще.")

# === Додавання акаунта DZ ===
add_user("DZ", "0910", "Зайдліч Данііл Максимович")

if __name__ == "__main__":
    main()
