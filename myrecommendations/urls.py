"""myrecommendations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
<<<<<<< HEAD
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
=======
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
>>>>>>> 314c1e3cfd5a2a31dc8fb54eb7c4bce031b4f13f
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
<<<<<<< HEAD
from django.views.static import serve
from django.conf import settings
=======
>>>>>>> 314c1e3cfd5a2a31dc8fb54eb7c4bce031b4f13f

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^myrestaurants/', include('myrestaurants.urls', namespace='myrestaurants')),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
]
<<<<<<< HEAD

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, })
    ]
=======
>>>>>>> 314c1e3cfd5a2a31dc8fb54eb7c4bce031b4f13f
