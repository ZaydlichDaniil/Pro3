import re
from collections import Counter

def filter_ips(input_file_path, output_file_path, allowed_ips):
    ip_counts = Counter()
    ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')

    try:
        with open(input_file_path, "r", encoding="utf-8") as infile:
            for line in infile:
                match = ip_pattern.search(line)
                if match:
                    ip = match.group()
                    if ip in allowed_ips:
                        ip_counts[ip] += 1
    except FileNotFoundError:
        print(f"Помилка: вхідний файл '{input_file_path}' не знайдено.")
        return
    except IOError as e:
        print(f"Помилка читання файлу '{input_file_path}': {e}")
        return

    try:
        with open(output_file_path, "w", encoding="utf-8") as outfile:
            for ip in allowed_ips:
                count = ip_counts.get(ip, 0)
                outfile.write(f"{ip} - {count}\n")
    except IOError as e:
        print(f"Помилка запису у файл '{output_file_path}': {e}")
