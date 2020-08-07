from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.check_out, name='check_out'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('cache_check_out_data/', views.cache_checkout_data, name='cache_check_out_data'),
    path('wh/', webhook, name='webhook'),
]
