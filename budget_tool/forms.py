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

    # def __init__(self, *args, **kwargs):
    #     super(TransactionForm, self).__init__(*args, **kwargs)
    #     self.user = kwargs.pop('user', None)
    #     import pdb; pdb.set_trace()
    #     # self.user is empty; "You would need to do something clever to return a class with the user value baked in from get_form."; https://stackoverflow.com/questions/28078419/django-modeladmin-get-queryset-from-modelform?
    #     self.fields['budget'].queryset = Transaction.objects.filter(budget__user__username=self.request.user.username)










