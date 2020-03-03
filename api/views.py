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
def profile(request):
    quantity = request.body.decode('utf8')
    quantity = json.loads(quantity)

    print(quantity)
    cost = calculate_cost(quantity)

    return JsonResponse(cost)


class MyFriend(View):
    def get(self, request):
        friend_list = list([1,2])
        return JsonResponse(friend_list, safe=False) 

    # To turn off CSRF validation (not recommended in production)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(MyFriend, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        print("hello")
        print("")
        print("")
        print("")
        print("")
        data = request.body.decode('utf8')
        data = json.loads(data)
        try:
            # new_friend = MyFriendList(friend_name=data["friend_name"], mobile_no=data["mobile_no"])
            # new_friend.save()
            return JsonResponse({"created": data}, safe=False)
        except:
            return JsonResponse({"error": "not a valid data"}, safe=False)