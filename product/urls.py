from django.urls import path, include
from product import views

urlpatterns = [
    path('', views.product_view), # /api/product
    path('inbound/', views.inbound_view),  # /api/product/inbound/
    path('outbound/', views.outbound_view),  # /api/product/outbound/
]
