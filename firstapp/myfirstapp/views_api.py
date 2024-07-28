from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import requests

@csrf_exempt
def consume_api_get(request):
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    data = response.json()
    return render(request, "Api-get.html", {'data': data})
