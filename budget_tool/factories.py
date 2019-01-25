"""This module contains class based on Factory."""
import factory
from django.contrib.auth.models import User
from budget_tool.models import Budget, Transaction


class UserFactory(factory.django.DjangoModelFactory):
    """Create a test user for writing tests."""

    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class BudgetFactory(factory.django.DjangoModelFactory):
    """Create a test budget for writing tests."""

    class Meta:
        model = Budget

    user = factory.SubFactory(UserFactory)
    name = factory.Faker('word')
    total_budget = 100.0
    remaining_budget = 100.0


class TransactionFactory(factory.django.DjangoModelFactory):
    """Create a test Transaction for writing tests."""

    class Meta:
        model = Transaction

    assigned_to = factory.SubFactory(UserFactory)
    budget = factory.SubFactory(BudgetFactory)
    transaction_type = 'deposit'
    amount = 15.0
    description = factory.Faker('paragraph')

