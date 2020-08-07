from django.urls import path
from . import views

urlpatterns = [
    path('', views.check_out, name='check_out'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
]