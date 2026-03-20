list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle_index = len(list_players) // 2 # деление на 2 команды

first_team = list_players[:middle_index] # список 1 команды
second_team = list_players[middle_index:] # список 2 команды

print(first_team) # вывод 1 списка
print(second_team) # вывод 2 списка
