"""maria_irma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from maria_irma_app import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('contacto/', views.contacto, name='contacto'),

    path('servicios/', views.servicios, name='servicios'),

    path('planos/', views.PlanoListView, name='list_plano'),
    path('planos/<slug:slug>', views.PlanoDetailView.as_view(), name='plano'),
    
    path('cabanas/', views.CabanaListView, name='list_cabana'),
    path('cabanas/<slug:slug>', views.CabanaDetailView.as_view(), name='detail_cabana'),

        

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
