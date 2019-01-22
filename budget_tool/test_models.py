from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .models import Budget, Transaction
from django.db import models
# from ..budget_project.factories import UserFactory, BudgetFactory, TransactionFactory


class TestBudgetModels(TestCase):
    """To test model Budget."""
    def setUp(self):
        # Fail to import Factory in factories.py:
        # self.budget = BudgetFactory(
        #     name='test name',
        #     description='test desc'
        # )

        self.user = User.objects.create_user('user_test', 'test@test.com', 'testuser123')
        self.budget = Budget.objects.create(name='test name', total_budget=0, remaining_budget=0, user=self.user)

    def test_default_budget_attrs(self):
        self.assertEqual(self.budget.name, 'test name')


class TestTransactionModels(TestCase):
    """To test model Transaction."""
    def setUp(self):
        # Fail to import Factory in factories.py:
        # self.budget = BudgetFactory(
        #     name='test name',
        #     description='test desc'
        # )

        self.user = User.objects.create_user('user_test', 'test@test.com', 'testuser123')
        self.budget = Budget.objects.create(name='test name', total_budget=0, remaining_budget=0, user=self.user)
        self.transaction = Transaction.objects.create(budget=self.budget, transaction_type='deposit', amount=0, description='test description')

    def test_default_transaction_attrs(self):
        self.assertEqual(self.transaction.amount, 0)





