from django.urls import path, include
from rest_framework import routers
from .views import PlotViewSet

router = routers.DefaultRouter()
router.register(r'plot', PlotViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('plot/', PlotViewSet.as_view(
        {'get': 'list', 'post': 'create'})),
    path('plot/<int:pk>/', PlotViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
        
    ))
]