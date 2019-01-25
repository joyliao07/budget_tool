"""This module create django forms."""
from django.forms import ModelForm
from django.db import models
from .models import Budget, Transaction


class BudgetForm(ModelForm):
    """To create budget-add form."""
    class Meta:
        model = Budget
        fields = ['name', 'total_budget', 'remaining_budget']


class TransactionForm(ModelForm):
    """To create transaction-add form."""
    class Meta:
        model = Transaction
        fields = ['budget', 'transaction_type', 'amount', 'description']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['budget'].queryset = Budget.objects.filter(user__username=self.user.username)
