from django.conf.urls import patterns, url
from django.views import generic
from stories import views


urlpatterns = patterns('',
    url(r'^$', views.StoryAddView.as_view(), name='story_list'),
)
