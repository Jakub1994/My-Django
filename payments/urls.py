from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.payments, name='payment'),
    path('paymentsuccess/<order_number>', views.payment_success, name='paymentsuccess'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]
