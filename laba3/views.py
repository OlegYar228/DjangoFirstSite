from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world!")


def table(request):
    return render(request, "pages/main/index.html")


def summ(request):
    if request.method == 'POST':
        number1 = int(request.POST['number1'])
        number2 = int(request.POST['number2'])
        result = number1 + number2
        return render(request, 'pages/summ/request.html', {'result': result})
    else:
        return render(request, 'pages/summ/index.html')


def string(request):
    if request.method == 'POST':
        str = request.POST['string']
        reverseStr = ""
        for char in str:
            reverseStr = char + reverseStr
        print(reverseStr)
        return render(request, 'pages/string/request.html', {'result': reverseStr})
    else:
        return render(request, 'pages/string/index.html')
