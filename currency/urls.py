from django.urls import path
from .views import USD,EUR,GBP

urlpatterns = [
    path("USD/",USD),
    path("EUR/",EUR),
    path("GBP/",GBP),
]
