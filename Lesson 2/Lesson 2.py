import random
"""
Задание 1
Выяснить тип результата выражений
"""
print("\nЗадание 1\n")
a = 15 * 3
b = 15 / 3
c = 15 // 2
d = 15 ** 2
print(f"Результат: {a}", "(", type(a), ")", " - тип первого результата выражения (15*3)\n"
                                            f"Результат: {b}", "(", type(b), ")",
      " - тип второго результата выражения (15/3)\n"
      f"Результат: {c}", "(", type(c), ")", " - тип третьего результата выражения (15//2)\n"
                                            f"Результат: {d}", "(", type(d), ")",
      " - тип четвертого результата выражения (15**2)\n")

"""
Задание 2/3
Необходимо обработать список — обособить каждое целое число кавычками и дополнить нулём до двух разрядов.
Сформировать из обработанного списка строку.
*Решить задачу 2 не создавая новый список.
*Подумать, какое условие записать, чтобы выявить числа среди элементов списка? 
*Как модифицировать это условие для чисел со знаком?
"""
print("Задание 2/3\n")
list1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(dir(list1))

print(f"Оригинальный список: {list1}\n")
print(f"This is second element: {list1[1]}", f"and this is its type {type(list[1])}\n")  # Пытался понять тип элемента

for i, typ in enumerate(list1):
    if typ.isdigit():
        if len(typ) == 1:
            list1[i] = '0' + list1[i]
    else:
        if typ[1:].isdigit():
            if len(typ[1:]) == 1:
                list1[i] = typ[0:1] + '0' + typ[1:]

print(f"Округление числовых значений до формата 00: {list1}")

list1[1:2] = ['"', list1[1], '"']
list1[5:6] = ['"', list1[5], '"']
list1[-2:-1] = ['"', list1[-2], '"']

print(f"Обособление каждого целого числа кавычками: {list1}\n")

# Знаю что дикий костыль, но по-другому сделать не смог
print(
    f"Результат: {list1[0]} {list1[1]}{list1[2]}{list1[3]} {list1[4]} {list1[5]}{list1[6]}{list1[7]} {list1[8]} "
    f"{list1[9]} {list1[10]} {list1[11]} {list1[12]}{list1[13]}{list1[14]} {list1[15]}\n")

"""
Задание 4
Сформировать и вывести на экран фразы из списка.
Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.
"""
print('Задание 4\n')
list2 = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in list2:
    names = i.split()
    print('Привет,', names[-1].lower().title(), end='!')
    print()

"""
Задание 5
Создать список, содержащий цены на товары.
"""

print("\n Задание 5\n")

# Инициализирую список с рандомно загенеринными дробными числами
prices_int = random.sample(range(0, 9999), 20)
print(f"Test purpose list: {prices_int}")
prices = [x / 100 for x in prices_int]
print(f"Это список велечин цен: {prices}\n")

print("Результат:")
pricesBackUp = prices
for i, x in enumerate(prices):
    prices[i] = str(x).split('.')
    prices[i][0] = prices[i][0] + ' руб'
    if len(prices[i]) > 1:
        if len(prices[i][1]) == 1:
            prices[i][1] = '0' + prices[i][1]
        prices[i][1] = prices[i][1] + ' коп'
    else:
        prices[i].append('00 коп')
    prices[i] = ' '.join(prices[i])
print(', '.join(prices))
prices.sort()
print(f"\nЭто сортированный список по велечине: {prices}\n")
if id(prices) == id(pricesBackUp):
    print("Доказательство того, что объект списка после сортировки остался тот же: ","id", id(prices), 'and', "id",
          id(pricesBackUp), 'равны\n')

pricesRev = []
for i in prices:
    pricesRev.append(i)
pricesRev.sort(reverse=True)
print(f"Развернутый по велечине список: {pricesRev}\n")
mostPrice = sorted(pricesRev)[-5:]
print(f"Цена 5-ти самых дорогих товаров: {mostPrice}")