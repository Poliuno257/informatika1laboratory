# TODO Напишите функцию find_common_participants
def find_common_participants(a, b, sep=','):
    structure_one = a.split(sep)  # создаём первый список раздельных имён
    structure_two = b.split(sep)  # создаём второй список раздельных имён
    jointly = set(structure_one).intersection(set(structure_two))  # ищем общие
    jointly1 = list(jointly)  # преобразовываем в список
    jointly1.sort()  # сортируем
    return jointly1  # выводим

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group), sep='|')
# TODO Провеьте работу функции с разделителем отличным от запятой
