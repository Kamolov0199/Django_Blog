from django.urls import path
from .views import Hoodie, Hoodie1, Hoodie2, Hoodie3, Hoodie4

urlpatterns = [
    path("", Hoodie),
    path("", Hoodie1),
    path("", Hoodie2),
    path("", Hoodie3),
    path("", Hoodie4),
]