"""vocdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth.views import LoginView, LogoutView

from .views import Index


admin.site.site_header = "Todos Administration"
admin.site.site_title = "Todos Administration"
admin.site.index_title = "Welcome to Todos Administration"


urlpatterns = [
    url(r'^$', Index.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/login/',
        LoginView.as_view(template_name=os.path.join('auth', 'login.html')),
        name="login"),
    url(r'^auth/logout/', LogoutView.as_view(), name="logout"),

    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^asana/', include('asana.urls', namespace='asana'))
]
