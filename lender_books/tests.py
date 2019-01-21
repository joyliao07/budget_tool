"""To test django project."""
from django.test import TestCase, RequestFactory
from .models import Book
from django.contrib.auth.models import User


class TestBookModel(TestCase):
    """To test book model."""
    def setUp(self):
        """To setup class."""
        self.user = User.objects.create_user('user_test', 'test@test.com', 'testuser123')
        self.book = Book.objects.create(title='Test Book 1', author='author 1', user=self.user)
        Book.objects.create(title='Test Book 2', author='author 2', user=self.user)

    def test_book_titles(self):
        """To test titles of books."""
        # import pdb; pdb.set_trace()
        one = Book.objects.get(title='Test Book 1')
        self.assertEqual(one.title, 'Test Book 1')

    def test_book_author(self):
        """To test author of books."""
        books = Book.objects.all()
        self.assertEqual(books[1].author, 'author 2')

    def test_book_status(self):
        """To test status of books."""
        one = Book.objects.get(title='Test Book 1')
        two = Book.objects.get(title='Test Book 2')
        self.assertEqual(one.status, 'available')
        self.assertEqual(two.status, 'available')

    def test_create_new_book(self):
        """To test creating a new book."""
        new_book = Book.objects.create(title='new', author='', user=self.user)
        self.assertEqual(new_book.title, 'new')


class TestBookViews(TestCase):
    """
    """
    def setUp(self):
        """To set up class."""
        self.request = RequestFactory()
        self.user = User.objects.create_user('user_test', 'test@test.com', 'testuser123')

        self.book = Book.objects.create(title='Test Book 1', author='author 1', user=self.user)
        Book.objects.create(title='Test Book 2', author='author 2', user=self.user)

    def test_list_view_context(self):
        """To test content of list_view."""
        from .views import book_list_view
        request = self.request.get('')
        request.user = self.user
        response = book_list_view(request)
        self.assertIn(b'Test Book 1', response.content)

    def test_list_view_status(self):
        """To test status code of list_view."""
        from .views import book_list_view
        request = self.request.get('')
        request.user = self.user
        response = book_list_view(request)
        self.assertEqual(200, response.status_code)

    def test_detail_view_context(self):
        """To test content of detail_view."""
        from .views import book_detail_view
        request = self.request.get('')
        request.user = self.user
        response = book_detail_view(request, self.book.id)
        self.assertIn(b'author 1', response.content)

    def test_detail_view_status_code_failure(self):
        """To test status code of detail_view."""
        from .views import book_detail_view
        from django.http import Http404
        request = self.request.get('')
        request.user = self.user

        with self.assertRaises(Http404):
            book_detail_view(request, '0')
