# article/views.py

from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Article


class ListArticleView(ListView):
    queryset = Article.published.all()
    template_name = 'article/article_list.html'


class DetailArticleView(DetailView):
    queryset = Article.published.all()
    template_name = 'article/article_detail.html'


def about(request):
    return render(request, 'about.html')
