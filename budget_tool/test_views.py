from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User
from .models import Budget, Transaction
from django.db import models
from .views import BudgetListView
from .factories import UserFactory, BudgetFactory, TransactionFactory


class TestBudgetViews(TestCase):
    """
    """
    def setUp(self):
        """To set up class."""
        self.user = UserFactory()
        self.user.set_password('secret')
        self.user.save()
        self.budget = BudgetFactory()
        self.budget.save()
        self.c = Client()

    def test_denied_if_no_login(self):
        res = self.c.get('/budget_tool/budget', follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'class="login-form container"', res.content)

    def test_home(self):
        res = self.c.get('/', follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'budget tool.', res.content)

    def test_view_list_when_logged_in(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )
        budget = BudgetFactory(user=self.user)
        res = self.c.get('/budget_tool/budget')
        self.assertIn(budget.name.encode(), res.content)

    def test_lists_only_owned_budgets(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )

        own_budget = BudgetFactory(user=self.user)
        other_budget = BudgetFactory()

        res = self.c.get('/budget_tool/budget')

        self.assertIn(own_budget.name.encode(), res.content)
        self.assertNotIn(other_budget.name.encode(), res.content)

    def test_transactions_listed_in_view(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )
        budget = BudgetFactory(user=self.user)
        transaction = TransactionFactory(budget=budget)
        res = self.c.get('/budget_tool/budget')
        description = transaction.description
        byte = description.encode()
        self.assertIn(byte, res.content)

    def test_create_view_adds_new_budget(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )
        form_data = {
            'user': 'test user',
            'name': 'Budget Two',
            'total_budget': 100.0,
            'remaining_budget': 1.0,
            'description': 'long description...'
        }
        res = self.c.post('/budget_tool/budget/add', form_data, follow=True)
        self.assertIn(b'Budget Two', res.content)

    def test_create_view_adds_new_transaction(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )
        form_data = {
            'assigned_to': self.user,
            'budget': 'test budget',
            'transaction_type': 'deposit',
            'amount': 8.0,
            'description': 'long description...',
        }
        res = self.c.post('/budget_tool/transaction/add', form_data, follow=True)
        self.assertIn(b'long description...', res.content)
