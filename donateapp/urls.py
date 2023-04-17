from django.urls import path

from . import views

urlpatterns = [

    # My donation page
    # path('spende/', views.donate, name='main-donate'),

    path('donation', views.donation_page, name='donateapp-paypal'),

    # Payment success

    path('payment-success', views.payment_success, name='donation-success'),

    # Payment failed

    path('payment-failed', views.payment_failed, name='donation-failed'),
   
]