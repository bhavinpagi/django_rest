import json

from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
from .models import Employee
from .serializers import EmployeeSerializer
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect


def index(request):
    return JsonResponse({"success": False, "data": "My second API"})



class Employees(APIView):
    def get(self, request):
        queryset = Employee.objects.all()
        serializer_class = EmployeeSerializer(queryset, many=True)
        return Response(data=serializer_class.data, status=200)
    
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(data=serializer.data, status=201)


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@csrf_exempt
def user_login(request):
    message = ""
    if request.method == "POST":
        print(request.body, "#######")
        request_data = json.loads(request.body)
        # csrf_token = request.POST.get('csrfmiddlewaretoken')
        username = request_data.get('username')
        password = request_data.get('password')

        username = User.objects.filter(username=username).first()
        print(username, type(username))
        is_authenticated = authenticate(request, username=username, password=password)
        print(is_authenticated)
        if is_authenticated:            
            login(request, user=username)
            tokens = get_tokens_for_user(username)
            return JsonResponse(tokens)