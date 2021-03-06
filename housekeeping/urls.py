"""housekeeping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from homepage import views as homepage_views
from testapp import views as testapp_views
from account import views as account_views
from django.views.static import serve
from housekeeping.settings import MEDIA_ROOT,MEDIA_URL
#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', homepage_views.welcome,name='welcome'),
    
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', homepage_views.index,name='index'),
    url(r'^teacher/$', homepage_views.view_teacher,name='teacher'),
    
    url(r'^register/$', account_views.register,name='register'),
    url(r'^accounts/login/$', account_views.login_view,name='login'),
    url(r'^accounts/logout/$', account_views.logout_view,name='logout'),
    url(r'^accounts/profile/$', homepage_views.index),# name = ? 

    url(r'^upload_file/$', testapp_views.upload_file,name='upload_file'),
    url(r'^listing/$', testapp_views.listing,name='listing'),

    url(r'^media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}),
]#+ static(MEDIA_URL, document_root=MEDIA_ROOT)
