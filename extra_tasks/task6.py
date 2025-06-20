"""
Створи клас Book, який має:
🔸 Поля:
title — назва книги
author — автор
pages — кількість сторінок

🔸 Методи:
description(self) — звичайний метод, повертає рядок типу:
"Назва: Гаррі Поттер, Автор: Дж.К. Ролінг, Сторінок: 500"

@staticmethod def is_long_book(pages) — статичний метод, який повертає:
True, якщо сторінок більше ніж 300
False — інакше
"""
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def description(self):
        return f"Назва: {self.title}, Автор: {self.author}, {self.pages}"

    @staticmethod
    def is_long_book(pages):
        if pages > 300:
            return True
        return False


book = Book("Гаррі Поттер", "Дж.К. Ролінг", 500)
print(book.description())                     # Назва: Гаррі Поттер, Автор: Дж.К. Ролінг, Сторінок: 500
print(Book.is_long_book(500))                 # True
print(Book.is_long_book(120))                 # False



