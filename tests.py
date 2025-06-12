from pip._internal.index import collector

from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    def test_set_book_genre(self):
        collector = BooksCollector()

        # 1. Добавляем книгу
        collector.books_genre = {"Гарри Поттер": ""}

        # 2. Устанавливаем жанр с помощью метода set_book_genre
        collector.books_genre["Гарри Поттер"] = "Фантастика"

        # 3. Проверяем, что жанр установился правильно
        assert collector.get_book_genre("Гарри Поттер") == "Фантастика"

    def test_get_book_genre(self):
        # Создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        # Название книги
        collector.books_genre = {"Гарри Поттер": ""}

        # Добавляем новую книгу
        collector.set_book_genre("Гарри Поттер", "Фантастика")

        assert collector.get_book_genre("Гарри Поттер") == "Фантастика"

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.books_genre = {"Шерлок Холмс" : ""}
        collector.books_genre = {"Гарри Поттер": ""}
        collector.books_genre["Шерлок Холмс"] = "Детективы"
        collector.books_genre["Гарри Поттер"] = "Фантастика"

        assert collector.get_books_with_specific_genre("Детективы") == ["Шерлок Холмс"]
        assert collector.get_books_with_specific_genre('Фантастика') == ["Гарри Поттер"]