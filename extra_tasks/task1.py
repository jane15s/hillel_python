"""
Дано список цілих чисел nums і ціле число target. Потрібно знайти індекси двох чисел у списку,
які в сумі дають target.

Ти можеш припустити, що буде тільки одна така пара,
і одне й те саме число не використовується двічі.

🔣 Приклад:

Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
# Бо nums[0] + nums[1] == 2 + 7 == 9
"""

# def twoSum(nums: list[int], target: int) -> list[int]:
#     i = 0
#     while i < len(nums) - 1:
#         j = i + 1
#         while j < len(nums):
#             if target == nums[i] + nums[j]:
#                 return [i, j]
#             j = j + 1
#         i = i + 1
#
def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


assert twoSum([2, 7, 11, 15], 9) == [0, 1]
assert twoSum([3, 2, 4], 6) == [1, 2]
assert twoSum([3, 3], 6) == [0, 1]

# print(twoSum([2, 7, 11, 15], 9)) # == [0, 1]
# print(twoSum([3, 2, 4], 6)) # == [1, 2]
# print(twoSum([3, 3], 6)) # == [0, 1]

# nums = [2, 7, 11, 15]
# target = 9
# new_list = []
# i = 0
# while i < len(nums) - 1:
#     if target == nums[i] + nums[i + 1]:
#         new_list.append([i, i + 1])
#         print(new_list)
#     i = i + 1