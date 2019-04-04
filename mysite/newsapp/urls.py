from django.urls import path, include
from django.views.generic import ListView, DetailView
from newsapp.models import Articles


urlpatterns = [
    path('', ListView.as_view(queryset=Articles.objects.all().order_by("-publdate")[:20]), name='news/posts.html'),
]
