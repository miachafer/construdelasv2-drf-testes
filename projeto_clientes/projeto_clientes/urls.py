from django.contrib import admin
from django.urls import path, include
from app_clientes.views import ClienteViewSet
from rest_framework import routers, serializers, viewsets

'''Criação de rota de urls para a viewset'''

router = routers.DefaultRouter()
router.register('clientes', ClienteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
