from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'),
        name='home'),

    url(r'^accounts/', include('allauth.urls')),

    url(r'^accounts/profile/$',
        TemplateView.as_view(template_name='accounts/profile.html'),
        name='accounts-profile'),

    url(r'^admin/', include(admin.site.urls)),
]
