from django.test import TestCase
from .models import Book
from django.urls import reverse


class BookModelTest(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title='Война и мир',
            author='Л. Н. Толстой',
            publication_date='1865-07-08',
        )

    def test_book_content(self):
        self.assertEqual(f'{self.book.title}', 'Война и мир')
        self.assertEqual(f'{self.book.author}', 'Л. Н. Толстой')
        print(f"Book title: {self.book.title}, \nAuthor: {self.book.author}")

    def test_book_appearance(self):
        self.assertEqual(str(self.book.publication_date), '1865-07-08')
        self.assertEqual(self.book.is_available, True)
        print(f"\nPublication date: {self.book.publication_date}, \nBook is available: {self.book.is_available}")

