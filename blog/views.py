from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "author": "Aleksander Brunsch",
        "title": "Ale poscik",
        "content": "Ale kontencik",
        "post_date": "dzisiaj"
    },
    {
        "author": "Piotr Stachnio",
        "title": "Ale poscik Piotra",
        "content": "Ale kontencik",
        "post_date": "dzisiaj"    
    }
]



def home(request):
    context = {
        "posts": posts
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html")


# Create your views here.
