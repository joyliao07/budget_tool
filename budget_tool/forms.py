from django.forms import ModelForm
from .models import Budget, Transaction


class BudgetForm(ModelForm):
    class Meta:
        model = Budget
        fields = ['name', 'total_budget', 'remaining_budget']


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['budget', 'transaction_type', 'amount', 'description']
    # def __init__(self, user=None, **kwargs):
    #     super(ExcludedDateForm, self).__init__(**kwargs)
    #     if user:
    #         self.fields['category'].queryset = models.Category.objects.filter(user=user)
