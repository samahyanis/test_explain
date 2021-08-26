from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView

from . import views
urlpatterns = [

    path('admin/', admin.site.urls),
    path('get_terriotry/',views.get_departement),
    path('get_departement_by_name/',views.get_departement_by_name),
]
