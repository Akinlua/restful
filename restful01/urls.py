"""restful01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

# from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('drones.urls')), 
    re_path(r'^api-auth/', include('rest_framework.urls')),
    # re_path(r'^', include('toys.urls')),
    # re_path(r'^v1/', include(('drones.urls', 'v1'), namespace='v1')),
    # re_path(r'^v1/api-auth/', include(('rest_framework.urls', 'rest_framework_v1'), namespace='rest_framework_v1')), 
    # re_path(r'^v2/', include(('drones.v2.urls','v2'), namespace='v2')), 
    # re_path(r'^v2/api-auth/', include(('rest_framework.urls','rest_framework_v2'), namespace='rest_framework_v2')),
]
