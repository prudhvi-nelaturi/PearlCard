from django.urls import path
from .views import FareCalculatorView

urlpatterns = [
    path('calculate/', FareCalculatorView.as_view(), name='calculate-fare'),
]
