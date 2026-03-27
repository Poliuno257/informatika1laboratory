salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

deficit = 0
money_capital = 0

for months in range(1,11): # создаём последовательсность месяцев
    deficit = spend - salary # считаем сколько не хватает
    if deficit > 0:
        money_capital += deficit
    spend = spend * (1 + increase) # увеличиваем расходы

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
