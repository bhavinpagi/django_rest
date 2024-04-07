from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('employees/', views.Employees.as_view(), name="employees"),
    path('user_login/', views.user_login, name="login")
]
