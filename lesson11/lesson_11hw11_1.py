"""
Напишіть функцію-генератор prime_generator, яка повертатиме прості числа.
Верхня межа цього діапазону визначається параметром цієї функції.

Наприклад, виклик функції

list(prime_generator(10)) повинен відповідати послідовності з чисел [2, 3, 5, 7] .

Наступне число в цій послідовності - 11 і воно більше 10 тому воно не потрапляє в цей ряд
"""

def prime_generator(end):
    for i in range(2, end + 1):
        prime_nums = True
        end_range = int(i ** 0.5)
        for j in range(2, end_range + 1):
            if i % j == 0:
                prime_nums = False
                break
        if prime_nums:
            yield  i


from inspect import isgenerator
gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
