from django.urls import path
from .views import BudgetDetailView, BudgetListView, BudgetCreateView, TransactionCreateView

urlpatterns = [
    path('budget', BudgetListView.as_view(), name='budget_view'),
    path('transaction/<int:id>', BudgetDetailView.as_view(), name='budget_detail'),
    path('budget/add', BudgetCreateView.as_view(), name='budget_create'),
    path('transaction/add', TransactionCreateView.as_view(), name='transaction_create'),
]
