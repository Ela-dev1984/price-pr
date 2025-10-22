from django.urls import path
from .views import usd,eur,gbp

urlpatterns = [
    path("USD/",usd),
    path("EUR/",eur),
    path("GBP/",gbp),
]
