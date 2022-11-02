"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

#Вариант 1 - с функцией sort():
def my_func(a, b, c):
    tmp_list = [a, b, c]
    tmp_list.sort(reverse=True)
    print(f'Заданы числа: {a}, {b}, {c}')
    return tmp_list[0] + tmp_list[1]

print(f'Сумма наибольших 2 аргументов: {my_func(4, 12, 5)}')

#Вариант 2 - без функции sort():
def my_func(a, b, c):
    print(f'Заданы числа: {a}, {b}, {c}')
    if a >= c and b >= c:
        return a + b
    elif b >= a and c >= a:
        return b + c
    elif a >= b and c >= b:
        return a + c

print(f'Сумма наибольших 2 аргументов: {my_func(13, 12, 19)}')
