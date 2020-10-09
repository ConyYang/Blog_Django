from typing import Dict, List
from .models import Post
from django.shortcuts import render

# dummy data here
# from django.http import HttpResponse

# Create your views here.
# posts = [
#     {
#         'author': 'Cony Yang',
#         'title': 'A Nice Meal',
#         'content': 'Beef and tomato noodles',
#         'date_posted': 'October 6, 2020'
#     },
#     {
#         'author': 'Lu Yao',
#         'title': 'A Nice Day',
#         'content': 'Today is a nice day',
#         'date_posted': 'October 7, 2020'
#     }
# ]


def home(request):
    context: Dict[str, List[Dict[str, str]]] = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    title = {'title': 'About'}
    return render(request, 'blog/about.html', title)
