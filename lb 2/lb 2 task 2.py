import hashlib
import os  # Не забудь этот импорт

def generate_file_hashes(*file_paths):
    hashes = {}

    print("Поточна директорія:", os.getcwd())  # Показывает, откуда запускается скрипт

    for path in file_paths:
        try:
            with open(path, "rb") as f:
                file_data = f.read()
                file_hash = hashlib.sha256(file_data).hexdigest()
                hashes[path] = file_hash
        except FileNotFoundError:
            print(f" Помилка: файл '{path}' не знайдено.")
        except IOError:
            print(f" Помилка: не вдалося прочитати файл '{path}'.")

    return hashes

# Приклад використання
hashes = generate_file_hashes("file1.txt", "file2.txt", "apache_logs.txt")

print("\n SHA-256 хеші файлів:")
for file, h in hashes.items():
    print(f"{file}: {h}")