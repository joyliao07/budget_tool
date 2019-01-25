"""This module contains tests on budget_rest_app."""
from django.test import TestCase, RequestFactory, Client
from .factories import UserFactory, BudgetFactory, TransactionFactory


class TestUserAPI(TestCase):
    """To test API endpoints and methods."""

    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('secret')
        self.user.save()
        self.budget = BudgetFactory()
        self.budget.save()
        self.c = Client()

    def test_user_registration(self):
        user = {
            'username': 'test_user',
            'email': 'user@user.com',
            'password': 'test_pw',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
        }
        response = self.client.post('/api/v1/register', user)
        self.assertIn(b'"username":"test_user"', response.content)

    def test_user_login(self):
        import json
        user = {
            'username': 'test_user',
            'email': 'user@user.com',
            'password': 'test_pw',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
        }
        self.client.post('/api/v1/register', user)
        response = self.client.post('/api/v1/login', user)
        token = json.loads(response.content)

        self.assertEqual(len(token['token']), 40)

    def test_user_registration_status_code(self):
        user = {
            'username': 'test_user',
            'email': 'user@user.com',
            'password': 'test_pw',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
        }
        response = self.client.post('/api/v1/register', user)
        self.assertEqual(response.status_code, 201)

    def test_user_login_status_code(self):
        user = {
            'username': 'test_user',
            'email': 'user@user.com',
            'password': 'test_pw',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
        }
        self.client.post('/api/v1/register', user)
        response = self.client.post('/api/v1/login', user)
        self.assertEqual(response.status_code, 200)

    def test_user_api_view(self):
        user_test = {
            'username': 'test_user',
            'email': 'user@user.com',
            'password': 'test_pw',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
        }
        self.client.post('/api/v1/register', user_test)
        response = self.client.get('/api/v1/user/3')
        self.assertIn(b'username', response.content)

    # def test_budget_list_view(self):
    #     # To Add a new budget and see if it is in budget_list:
    #     self.c.login(
    #         username=self.user.username,
    #         password='secret'
    #     )
    #     form_data = {
    #         'user': 'test user',
    #         'name': 'Budget Two',
    #         'total_budget': 100.0,
    #         'remaining_budget': 1.0,
    #         'description': 'long description...'
    #     }
    #     self.c.post('/budget_tool/budget/add', form_data, follow=True)
    #     res = self.c.post('/budget_tool/budget/add', form_data, follow=True)
    #     res2 = self.client.get('api/v1/budget/', form_data, follow=True)
    #     import pdb; pdb.set_trace()
    #     self.assertIn(b'Budget Two', res.content)
