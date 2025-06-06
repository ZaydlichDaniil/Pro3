import hashlib
from datetime import datetime

# Базовий клас користувача
class User:
    def __init__(self, username, password, is_active=True):
        self.username = username
        self.password_hash = self._hash_password(password)
        self.is_active = is_active

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password):
        return self._hash_password(password) == self.password_hash

# Адміністратор
class Administrator(User):
    def __init__(self, username, password, permissions=None):
        super().__init__(username, password)
        self.permissions = permissions if permissions else []

    def add_permission(self, permission):
        if permission not in self.permissions:
            self.permissions.append(permission)

    def has_permission(self, permission):
        return permission in self.permissions

# Звичайний користувач
class RegularUser(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.last_login = None

    def update_last_login(self):
        self.last_login = datetime.now()

# Гість
class GuestUser(User):
    def __init__(self, username="guest0", password="12345"):
        super().__init__(username, password=password, is_active=True)
        self.limited_access = True

# Контроль доступу
class AccessControl:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        if user.username in self.users:
            print(f"Користувач '{user.username}' вже існує.")
        else:
            self.users[user.username] = user
            print(f"Користувача '{user.username}' додано.")

    def authenticate_user(self, username, password):
        user = self.users.get(username)
        if user and user.verify_password(password):
            if user.is_active:
                print(f"\n✅ Успішна автентифікація: {username}")
                if isinstance(user, RegularUser):
                    user.update_last_login()
                return user
            else:
                print(f"⛔ Користувач '{username}' неактивний.")
        else:
            print(f"❌ Невірний логін або пароль.")
        return None

# === Консольне меню ===
def login_interface(ac):
    print("\n=== Вхід у систему ===")
    username = input("Логін: ")
    password = input("Пароль: ")
    user = ac.authenticate_user(username, password)
    if user:
        print(f"Ви увійшли як {user.username}")
        if isinstance(user, Administrator):
            print("Роль: Адміністратор")
        elif isinstance(user, RegularUser):
            print("Роль: Звичайний користувач")
        elif isinstance(user, GuestUser):
            print("Роль: Гість")
    else:
        print("Спроба входу не вдалася.")

# === Створення користувачів і запуск ===
ac = AccessControl()

admin = Administrator("danya09", "0910", ["add_user", "edit_settings"])
user = RegularUser("vanya11", "1100")
guest = GuestUser(username="guest0")  # пароль: 12345

ac.add_user(admin)
ac.add_user(user)
ac.add_user(guest)

login_interface(ac)
