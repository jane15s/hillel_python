"""
Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.

Декілька правил:

ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
підсумкова довжина hashtag має бути не більше 140 символів.
кожне слово починається з великої літери.
якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.
Приклади:

'Python Community' -> #PythonCommunity
'i like python community!' -> #ILikePythonCommunity
'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes
"""
import string

input_for_hashtag = input("write whatever to convert it into hashtag: ")
for char in string.punctuation:
    input_for_hashtag = input_for_hashtag.replace(char, "")
words = input_for_hashtag.split()
titled_words = [word.title() for word in words]
hashtag = "#" + "".join(titled_words)
print(hashtag[:140])

