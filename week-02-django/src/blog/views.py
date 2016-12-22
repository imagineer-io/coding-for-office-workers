# from django.http import HttpResponse
from django.shortcuts import render
# from random import randint
# Create your views here.

def index(request):
    # random_number = randint(1, 10)
    # return HttpResponse("Hello, world. {}".format(random_number))
    # return HttpResponse("Hello, world. You're at the index.")
    name = "marco"
    return render(request, "index.html", { "name" : name })
