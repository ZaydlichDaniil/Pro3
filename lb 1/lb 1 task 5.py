import hashlib

# Функція хешування пароля
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# База користувачів: login → {"password": ..., "name": ...}
users = {
    "danya09": {
        "password": hash_password("09102006"),
        "name": "Зайдліч Данііл Максимович"
    },
    "olga_k": {
        "password": hash_password("12345olga"),
        "name": "Коваль Ольга Степанівна"
    }
}

def authenticate():
    login = input("Введіть логін: ")
    if login not in users:
        print("Користувача не знайдено.")
        return

    password = input("Введіть пароль: ")
    hashed_input = hash_password(password)

    if hashed_input == users[login]["password"]:
        print(f"Вітаємо, {users[login]['name']}! Аутентифікація успішна.")
    else:
        print("Неправильний пароль.")

# Приклад виклику
authenticate()