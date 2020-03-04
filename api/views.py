from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.views import View
import json
from .utils import calculate_cost
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.

@api_view(['GET', 'POST'])
def getCost(request):
    quantity = request.body.decode('utf8')
    quantity = json.loads(quantity)
    # print(quantity)
    cost = calculate_cost(quantity)
    return JsonResponse(cost)

