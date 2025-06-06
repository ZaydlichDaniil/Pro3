# Початковий інвентар
inventory = {
    "яблука": 10,
    "банани": 3,
    "молоко": 7,
    "хліб": 2,
    "сир": 5
}

def update_inventory(product_name, quantity_change):
    """
    Оновлює інвентар:
    - додає або віднімає кількість продукту
    - якщо продукту не існує — додає його
    """
    if product_name in inventory:
        inventory[product_name] += quantity_change
    else:
        inventory[product_name] = quantity_change

    # Якщо кількість стала < 0 — ставимо 0
    if inventory[product_name] < 0:
        inventory[product_name] = 0

# Приклади оновлення
update_inventory("яблука", -4)
update_inventory("печиво", 8)
update_inventory("хліб", -1)

# Знаходимо продукти з кількістю < 5
low_stock = [product for product, qty in inventory.items() if qty < 5]

# Вивід
print("Оновлений інвентар:", inventory)
print("Продукти з кількістю менше 5:", low_stock)