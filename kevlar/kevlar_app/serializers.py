from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Employee
        fields = ['id', 'last_name', 'first_name', 'patronymic',
                  'employment_date', 'level', 'position',
                  'monthly_wage', 'total_wage', 'authorities', 'owner']


class UserSerializer(serializers.ModelSerializer):
    employees = serializers.PrimaryKeyRelatedField(many=True,
                                                   queryset=Employee.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'employees']
