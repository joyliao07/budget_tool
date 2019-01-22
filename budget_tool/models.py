from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils import timezone
from django.db import models


class Budget(models.Model):
    """To create model Budget."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budgets')
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=180, default='Untitled Budget Name')
    total_budget = models.FloatField(blank=True)
    remaining_budget = models.FloatField(blank=True)

    def __repr__(self):
        return '<Budget: {}>'.format(self.name)

    def __str__(self):
        return '{}'.format(self.name)

    def remaining(self):

        pass


class Transaction(models.Model):
    """To create model Transaction."""
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions', null=True, blank=True)
    id = models.AutoField(primary_key=True)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='transactions')

    T_TYPE = (
        ('withdrawal', 'WITHDRAWAL'),
        ('deposit', 'DEPOSIT'),
    )
    transaction_type = models.CharField(max_length=25, choices=T_TYPE)
    amount = models.FloatField(default=0)
    description = models.CharField(max_length=180, default='Transaction Description')

    def __repr__(self):
        return '<Transaction: {} | {}>'.format(self.transaction_type, self.amount)

    def __str__(self):
        return '{} | {}'.format(self.transaction_type, self.amount)
