from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def homePageView(request):
    return render(request, 'index.html')

def barChart(request):
    if request.method == 'GET':
        response =  {}
        response["labels"] = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
        response["data"] = [12, 19, 3, 5, 2, 30]
    return JsonResponse(response)
