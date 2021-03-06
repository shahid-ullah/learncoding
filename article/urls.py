# article/urls.py

from django.urls import path

from .views import DetailArticleView, ListArticleView, about

app_name = 'article'
urlpatterns = [
    path('', ListArticleView.as_view(), name='article_list'),
    # path('detail/<int:pk>/<slug:slug>/', DetailArticleView.as_view(), name='article_detail'),
    path('detail/<slug:slug>/', DetailArticleView.as_view(), name='article_detail'),
    path('about/', about, name='about'),
    ]
