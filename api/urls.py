from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from api import settings

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='territory/index.html')),

    path('admin/', admin.site.urls),
    path('territory/',include("territory.urls")),
]

if True:
    urlpatterns+=static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)
