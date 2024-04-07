from django.db import models

class Department(models.Model):
    dept_name = models.CharField(max_length=20)
    head_quaters = models.CharField(max_length=20)
    floor = models.IntegerField()


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    salary = models.FloatField()
    date_of_joining = models.DateField()
    is_active = models.BooleanField()
    shift_timing = models.CharField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)