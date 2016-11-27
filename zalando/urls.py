from django.conf.urls import url
from . import views

app_name = 'zalando'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.ArticleDetailView.as_view(), name='detail'),
]
