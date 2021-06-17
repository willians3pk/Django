"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    # incluindo o arquivo de urls do app 'produtos', então quando for digitado na 
    # url do navegador "produtos/" ele vai ser direcionado pra url do app 'produtos'.
    path("produtos/", include("produtos.urls", namespace="produtos")), 
    # caminho para servir arquivos
    url(r'^img/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
