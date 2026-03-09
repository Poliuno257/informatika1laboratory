numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

resultone = sum(numbers[:4:]) # сумма первой части элементов списка
resulttwo = sum(numbers[5:20]) # сумма второй части элементов списка
resultthree = resultone + resulttwo # сумма двух частей списка
resulfour = resultthree / len(numbers) # среднее арифметическое элементов списка
numbers[4] = resulfour # замена нужного элемента

print("Измененный список:", numbers)

