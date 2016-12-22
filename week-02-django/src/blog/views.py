# from django.http import HttpResponse
from django.shortcuts import render
# from random import randint
from .models import Article
# Create your views here.

def index(request):
    # random_number = randint(1, 10)
    # return HttpResponse("Hello, world. {}".format(random_number))
    # return HttpResponse("Hello, world. You're at the index.")

    # name = "marco"
    # return render(request, "index.html", { "name" : name })
    article_list = Article.objects.all()
    # Article.objects.create(
    #     title="hello",
    #     contents="this is test",
    #     view_count=0
    # )
    ctx = {
        "article_list" : article_list
    }
    return render(request, "index.html", ctx)
