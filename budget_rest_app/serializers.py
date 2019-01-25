from django.contrib.auth.models import User
from budget_tool.models import Budget, Transaction
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """To serialize the fields in User model."""
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        user = super().create({
            'username': validated_data['username'],
            'email': validated_data['email'],
            'first_name': validated_data['first_name'],
            'last_name': validated_data['last_name'],
        })

        user.set_password(validated_data['password'])
        user.save()
        return user


class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    """To serialize the fields in Budget model."""
    # owner is the user name in database:
    owner = serializers.ReadOnlyField(source='user.username')

    # user will be something like "http://localhost:8000/api/v1/user/1":
    user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)

    class Meta:
        model = Budget
        fields = ('owner', 'id', 'user', 'name', 'total_budget', 'remaining_budget')


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    """To serialize the fields in Transaction model."""
    budget = serializers.HyperlinkedRelatedField(view_name='budget-detail-api', read_only=True)

    class Meta:
        model = Transaction
        fields = ('id', 'assigned_to', 'budget', 'transaction_type', 'description', 'amount')
