"""meuPrimeiroProjeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from .views import hello
from .views import articles
from .views import recuperarPessoa
from django.conf import settings
from django.conf.urls.static import static
from .clientes import urls as clientes_urls

urlpatterns = [
    path('hello/', hello),
    path('articles/<int:year>', articles),
    path('admin/', admin.site.urls),
    path('pessoa/<str:nome>', recuperarPessoa),
    path('persons/', include(clientes_urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)