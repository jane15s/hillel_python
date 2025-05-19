"""
Для списку цілих чисел потрібно знайти суму елементів із парними індексами [0-й, 2-й, 4-й ітд],
потім перемножити цю суму на останній елемент вхідного масиву.
Не забудьте, що перший елемент масиву має індекс 0.
Для порожнього масиву результат завжди 0.

Пояснення:
[0, 1, 7, 2, 4, 8] => (0 + 7 + 4) * 8 = 88

Приклад:
[1, 3, 5] => 30
[6] => 36
[] => 0
"""

matrix = [
    [1, 3, 5], # 0
    [6], # 1
    [] # 2
]

for some_list in matrix:
    if some_list: # if list is not empty
        result = 0 # result value to start
        for i in some_list[::2]: # for element of some_list list where step is 2
            result = result + i # summing 0 with first element with even index (0) + second...(2)
        final_result = result * some_list[-1]
    else:
        final_result = 0
    print(final_result)
