# TODO Напишите функцию для поиска индекса товара
def find_index(a, b):
    for index, element in enumerate(a):  # подставляем под все элементы индексы
        if element == b:  # сравниваем подходит ли элемент под искомый
            return index  # пишет только индекс, а не кортеж
    return None  # если не подошёл элемент(не найден), то возвращает None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
