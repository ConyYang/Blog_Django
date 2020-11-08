from typing import Dict, List
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        # check if is current user
        if self.request.user == post.author:
            # let allow post
            return True
        return False


class PostDeleteView(DeleteView, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    # the success_redirect url is the homepage.
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        # check if is current user
        if self.request.user == post.author:
            # let allow post
            return True
        return False


def about(request):
    title = {'title': 'About'}
    return render(request, 'blog/about.html', title)

