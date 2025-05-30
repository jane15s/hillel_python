"""
Функція second_index приймає як параметри 2 рядки. Вам необхідно знайти індекс другого входження шуканого рядка у рядку для пошуку.

Розберемо перший приклад, де необхідно знайти друге входження "s" в слові "sims". Якби нам треба було знайти її перше входження, то тут все просто: за допомогою функції index або find ми можемо дізнатися, що "s" - це перший символ у слові "sims", а значить індекс першого входження дорівнює 0. Але нам Необхідно визначити другу "s", а вона четверта за рахунком. Значить індекс другого входження (і у відповідь питання) дорівнює 3.

Рядок, який потрібно знайти, може складатися з кількох символів.

Input: Два рядки (String).

Output: Int or None

"""

def second_index(text, some_str):
    find_first = text.find(some_str)
    if find_first == -1:
        return None
    find_second = text.find(some_str, find_first +1)
    if find_second == -1:
        return None
    return int(find_second)
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')

# print(second_index("sims", "s"))# == 3, 'Test1'
# print(second_index("find the river", "e"))# == 12, 'Test2'
# print(second_index("hi", "h")) # is None, 'Test3'
# print(second_index("Hello, hello", "lo")) # == 10, 'Test4'



# text = "find the river"
# some_str = "e"
# lst = []
# for index, char in enumerate(text):
#     if char == some_str:
#         lst.append(index)
#
# if len(lst) >= 2:
#     answer = int(lst[1])
#     print(answer)

# def second_index(text, some_str):
#     lst = []
#     for index, char in enumerate(text):
#         if char == some_str:
#             lst.append(index)
#
#     if len(lst) >= 2:
#        return int(lst[1])
#     else:
#         return None