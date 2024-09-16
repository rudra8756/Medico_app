from django.shortcuts import render
from django .http import HttpResponse

# Create your views here.

def register(request):
    return HttpResponse("This is registration page")

def login(request):
    return HttpResponse("This is login page")

def home(request):
    return render(request, 'index.html')

def calc(request):
    return render(request,'arith.html')

def add(request):
    n1 =  int(request.GET['num1'])
    n2 =  int(request.GET['num2'])
    result = n1 + n2
    return render(request, "result.html",{'res':result})
