from decimal import Decimal
from django.test import TestCase
from rest_framework.test import APITestCase

from .models import Book


class BookTestCase(TestCase):
    def setUp(self):
        Book.objects.create(name="Harry Potter", price=49000)
        Book.objects.create(name="Science", price=39000)

    def test_book_name_price(self):
        potter = Book.objects.get(name="Harry Potter")
        science = Book.objects.get(name="Science")

        self.assertEqual(potter.price, Decimal('49000.00'))
        print('jj')
        self.assertEqual(science.price, Decimal('39000'))
        print('asljkd')

