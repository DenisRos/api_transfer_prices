from django.urls import path

from .views import TransferViewSet

urlpatterns = [
    path('transfer/<str:name_srv>/<str:username>/<str:password>', TransferViewSet, name = 'transfer'),
] 
