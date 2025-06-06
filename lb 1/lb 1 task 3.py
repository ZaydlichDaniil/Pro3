# Список продажів
sales = [
    {"продукт": "яблука", "кількість": 30, "ціна": 10},
    {"продукт": "банани", "кількість": 50, "ціна": 5},
    {"продукт": "яблука", "кількість": 20, "ціна": 10},
    {"продукт": "молоко", "кількість": 15, "ціна": 20},
    {"продукт": "хліб", "кількість": 40, "ціна": 8},
    {"продукт": "молоко", "кількість": 40, "ціна": 20}
]

def calculate_total_revenue(sales_list):
    """
    Обчислює загальний дохід для кожного продукту
    """
    revenue = {}
    for sale in sales_list:
        product = sale["продукт"]
        total = sale["кількість"] * sale["ціна"]
        if product in revenue:
            revenue[product] += total
        else:
            revenue[product] = total
    return revenue

# Розрахунок доходу
total_revenue = calculate_total_revenue(sales)

# Продукти з доходом > 1000
high_earning_products = [product for product, amount in total_revenue.items() if amount > 1000]

# Вивід
print("Загальний дохід по продуктах:", total_revenue)
print("Продукти з доходом понад 1000:", high_earning_products)