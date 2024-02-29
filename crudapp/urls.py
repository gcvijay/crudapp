"""crudapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from app1 import views
from django.conf import settings
from django.conf.urls.static import static
#from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.registartion,name = 'registartion'),
    path('create_daata/',views.create_daata,name = 'create_daata'),
    path('retrieve',views.retrieve,name="retrieve"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('update/<int:id>',views.update,name="update"),
    path(r'^delete_product/(?P<pk>[0-9]+)/$', views.delete,name="delete"),
    path('email_send/<int:id>',views.email_send,name = 'email_send'),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)