from typing import Dict, List

from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'author': 'Cony Yang',
        'title': 'A Nice Meal',
        'Content': 'Beef and tomato noodles',
        'date_posted': 'October 6, 2020'
    },
    {
        'author': 'Lu Yao',
        'title': 'A Nice Day',
        'Content': 'Today is a nice day',
        'date_posted': 'October 7, 2020'
    }
]


def home(request):
    context: Dict[str, List[Dict[str, str]]] = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    title = {'title': 'About'}
    return render(request, 'blog/about.html', title)
