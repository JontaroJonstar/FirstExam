from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def add(request, num1, num2):
    return HttpResponse(num1 + num2)

def minus(request, num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    return HttpResponse(num1 - num2)

def div(request, num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        if num2 == 0:
            return HttpResponse("Error: Cannot divide by zero")
        result = num1 / num2
        return HttpResponse(round(result))
    except ValueError:
        return HttpResponse("Error: Invalid input")
    except ZeroDivisionError:
        return HttpResponse("Error: Cannot divide by zero")

