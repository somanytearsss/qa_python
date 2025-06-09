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

        # Название книги
        name = 'Гарри Поттер'

        collector.add_new_book(name)
        collector.set_book_genre(name, 'Фантастика')
        assert collector.books_genre[name] == 'Фантастика'

    def test_get_book_genre(self):
        # Создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        # Название книги
        name = 'Гарри Поттер'

        # Добавляем новую книгу
        collector.add_new_book(name)

        # Устанавливаем жанр книги
        genre = 'Фантастика'

        collector.set_book_genre(name, genre)

        # Проверяем, что метод get_book_genre возвращает правильный жанр
        returned_genre = collector.get_book_genre(name)
        assert returned_genre == genre