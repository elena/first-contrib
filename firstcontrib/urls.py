from django.conf.urls import patterns, include, url
from django.views import generic

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('stories.urls')),

    url(r'^success$', generic.TemplateView.as_view(template_name="about.html"),
                      name='about'),

    url(r'^about$', generic.TemplateView.as_view(template_name="success.html"),
                      name='story_success'),

    (r'^ckeditor/', include('ckeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
