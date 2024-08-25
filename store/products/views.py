from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def getData(request):
    return JsonResponse({
        "name" : "Ansar"
    })
    # return Response(
    #     {
    #     "name" : "Ansar"
    # }
    # )