from django.forms import ModelForm
from django.db import models
from .models import Budget, Transaction


class BudgetForm(ModelForm):
    class Meta:
        model = Budget
        fields = ['name', 'total_budget', 'remaining_budget']


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['budget', 'transaction_type', 'amount', 'description']


# class TransactionSub(models.TransactionForm):
#     def __init__(self, *args, **kwargs):
#         kwargs['max_length'] = 104
#         super().__init__(*args, **kwargs)

