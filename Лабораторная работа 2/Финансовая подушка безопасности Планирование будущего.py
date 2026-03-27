money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0

while True:
    deficit = spend - salary  # считаем сколько не хватает
    if deficit > 0:
        money_capital -= deficit # берём из подушки безопастности
    if money_capital < 0: # подушка безопастности закончилась
        break
    months += 1
    spend = spend * (1 + increase) # увеличиваем расходы

print("Количество месяцев, которое можно протянуть без долгов:", months) # выводим нужное значение
