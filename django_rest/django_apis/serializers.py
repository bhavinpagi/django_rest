from rest_framework import serializers

from .models import Employee, Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):

    # department = DepartmentSerializer()
    class Meta:
        model = Employee
        # fields = ['first_name', 'last_name']
        fields = '__all__'
        # exclude = ['salary', 'date_of_joining']
