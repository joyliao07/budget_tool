from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .models import Budget, Transaction
from django.db import models
# from ..budget_project.factories import UserFactory, BudgetFactory, TransactionFactory

class TestBudgetViews(TestCase):
    """
    """
    def setUp(self):
        """To set up class."""
        self.request = RequestFactory()
        self.user = User.objects.create_user('user_test', 'test@test.com', 'testuser123')
        self.budget = Budget.objects.create(name='test name', total_budget=0, remaining_budget=0, user=self.user)

    def test_budget_list_view_context(self):
        """To test content of budget_list."""
        from .views import BudgetListView
        # request = self.request.get('')
        # request.user = self.user
        # response = BudgetListView()
        # self.assertIn(b'0', response.content)
        pass

