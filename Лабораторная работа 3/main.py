# TODO  Напишите функцию count_letters
def count_letters(text):
    letter_counts = {}
    for char in text:
        if char.isalpha():  # Проверяет, является ли символ буквой
            lower_char = char.lower()  # Приводит букву к нижнему регистру
            if lower_char in letter_counts:
                letter_counts[lower_char] += 1
            else:
                letter_counts[lower_char] = 1
    return letter_counts

# TODO Напишите функцию calculate_frequency
def calculate_frequency(letter_counts):
    total_letters = sum(letter_counts.values())  # Суммируем все подсчитанные буквы
    if total_letters == 0:
        return {}
    frequency = dict()
    for letter, count in letter_counts.items():
        frequency[letter] = count / total_letters  # Рассчитываем частоту
    return frequency

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте

letter_counts_result = count_letters(main_str)
letter_frequencies = calculate_frequency(letter_counts_result)
items = list(letter_frequencies.items())
items.sort()  # Сортируем по алфавиту
for letter, frequency in items:
    print(f"{letter}: {frequency:.2f}")  # Выводим с двумя знаками после запятой
