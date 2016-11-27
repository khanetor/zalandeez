from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article


# Create your views here.
class IndexView(ListView):
    model = Article
    template_name = 'zalando/index.html'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'zalando/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        return context
