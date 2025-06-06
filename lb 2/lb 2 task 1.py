def analyze_log_file(log_file_path):
    response_codes = {}

    try:
        with open(log_file_path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) > 8:
                    # У логах Apache код відповіді зазвичай знаходиться на 9-й позиції
                    code = parts[8]
                    if code.isdigit():
                        response_codes[code] = response_codes.get(code, 0) + 1
    except FileNotFoundError:
        print(f"Помилка: файл '{log_file_path}' не знайдено.")
        return {}
    except IOError:
        print(f"Помилка: не вдалося прочитати файл '{log_file_path}'.")
        return {}

    return response_codes

# Приклад використання
log_path = "apache_logs.txt"
result = analyze_log_file(log_path)
print("Результати аналізу лог-файлу:", result)