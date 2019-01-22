from django.urls import path
from .views import BudgetDetailView, BudgetListView

urlpatterns = [
    path('budget', BudgetListView.as_view(), name='budget_view'),
    path('transaction/<int:id>', BudgetDetailView.as_view(), name='budget_detail'),
]
