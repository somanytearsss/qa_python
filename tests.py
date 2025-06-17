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
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    def test_set_book_genre__valid_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        assert collector.get_book_genre("Гарри Поттер") == "Фантастика"

    @pytest.mark.parametrize("book_title, genre", [
        ("Молодость", "Комедии")])
    def test_get_book_genre__returns_correct_genre(self, book_title, genre):
        collector = BooksCollector()
        collector.add_new_book(book_title)
        collector.set_book_genre(book_title, genre)
        assert collector.get_book_genre(book_title) == genre

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Шерлок Холмс")
        collector.set_book_genre("Шерлок Холмс", "Детективы")
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")

        assert collector.get_books_with_specific_genre("Детективы") == ["Шерлок Холмс"]
        assert collector.get_books_with_specific_genre("Фантастика") == ["Гарри Поттер"]

    def test_get_books_genre__returns_full_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book("Шерлок Холмс")
        collector.set_book_genre("Шерлок Холмс", "Детективы")
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")

        assert collector.get_books_genre() == {
            "Шерлок Холмс": "Детективы",
            "Гарри Поттер": "Фантастика"
        }

    def test_get_books_for_children__filters_age_restricted_genres(self):
        collector = BooksCollector()

        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")  # Допустимый для детей

        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")  # Не для детей

        collector.add_new_book("Шерлок Холмс")
        collector.set_book_genre("Шерлок Холмс", "Детективы")  # Не для детей

        collector.add_new_book("Том и Джерри")
        collector.set_book_genre("Том и Джерри", "Мультфильмы")  # Допустимый для детей

        # Проверяем, что метод возвращает только книги для детей
        children_books = collector.get_books_for_children()

        # Проверяем, что ожидаемые книги находятся в списке
        assert "Гарри Поттер" in children_books
        assert "Том и Джерри" in children_books

        # Проверяем, что нежелательные книги не находятся в списке
        assert "Оно" not in children_books
        assert "Шерлок Холмс" not in children_books

    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")

        assert "Гарри Поттер" in collector.favorites

    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book("Мастер и Маргарита")
        collector.add_book_in_favorites("Мастер и Маргарита")
        collector.delete_book_from_favorites("Мастер и Маргарита")
        
        assert "Мастер и Маргарита" not in collector.favorites

    @pytest.mark.parametrize("books, expected_favorites", [
        (["Война и мир", "Анна Каренина"], ["Война и мир", "Анна Каренина"])
    ])
    def test_get_list_of_favorites_books__returns_all_favorites(self, books, expected_favorites):
        collector = BooksCollector()

        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)

        assert collector.get_list_of_favorites_books() == expected_favorites








