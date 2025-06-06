# Початковий словник задач
tasks = {
    "підготувати звіт": "в процесі",
    "відправити email": "виконано",
    "розробити презентацію": "очікує"
}

def add_task(name, status="очікує"):
    """
    Додає нову задачу з заданим статусом (за замовчуванням "очікує")
    """
    tasks[name] = status

def remove_task(name):
    """
    Видаляє задачу, якщо вона існує
    """
    if name in tasks:
        del tasks[name]

def update_task_status(name, new_status):
    """
    Оновлює статус існуючої задачі
    """
    if name in tasks:
        tasks[name] = new_status

def get_pending_tasks():
    """
    Повертає список задач зі статусом "очікує"
    """
    return [name for name, status in tasks.items() if status == "очікує"]

# Приклади використання:
add_task("зробити резервне копіювання")
update_task_status("підготувати звіт", "виконано")
remove_task("відправити email")

# Отримання списку задач зі статусом "очікує"
pending = get_pending_tasks()

# Вивід
print("Усі задачі:", tasks)
print("Задачі, що очікують:", pending)