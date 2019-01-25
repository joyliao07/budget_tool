"""This module contains views based on rest framework."""
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import (
    UserSerializer,
    User,
    BudgetSerializer,
    Budget,
    TransactionSerializer,
    Transaction,
    )


class RegisterApiView(generics.CreateAPIView):
    """To set up register api view."""
    permission_classes = ''
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer


class UserApiView(generics.RetrieveAPIView):
    """To set up user api view."""
    permission_classes = ''
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['pk'])


class BudgetListApiView(generics.ListCreateAPIView):
    """To set up budget list api view."""
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = BudgetSerializer

    def get_queryset(self):
        return Budget.objects.filter(
            user__username=self.request.user.username)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


class BudgetDetailApiView(generics.RetrieveAPIView):
    """To set up budget detail api view."""
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = BudgetSerializer

    def get_queryset(self):
        return Budget.objects.filter(
            user__username=self.request.user.username)


class TransactionListApiView(generics.ListCreateAPIView):
    """To set up transaction list api view."""
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(
            budget__user__username=self.request.user.username)


class TransactionDetailApiView(generics.RetrieveAPIView):
    """To set up transaction detail api view."""
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(
            budget__user__username=self.request.user.username)
