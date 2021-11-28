from django.urls import path,include
from .views import IP_Interface, IP_Listing
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', csrf_exempt(IP_Interface.as_view()), name='ip_interface'),
    path('ip_listing', IP_Listing.as_view(), name='ip_listing'),
]
