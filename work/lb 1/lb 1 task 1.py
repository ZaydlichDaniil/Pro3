def word_frequency(text):
    # Розділяємо текст на слова, прибираючи пунктуацію та переводячи все у нижній регістр
    words = text.lower().split()
    words = [word.strip('.,!?;:"()[]{}') for word in words]

    # Створюємо словник для підрахунку кількості кожного слова
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    # Список слів, які зустрічаються більше 3 разів
    frequent_words = [word for word, count in freq.items() if count > 3]

    # Повертаємо словник частот і друкуємо список частих слів
    print("Слова, що зустрічаються більше 3 разів:", frequent_words)
    return freq

# Приклад використання
text = "Це приклад тексту. Текст має багато слів. Деякі слова повторюються. Слова, слова, слова. Текст — це набір слів."
frequency_dict = word_frequency(text)
print("Словник частот:", frequency_dict)