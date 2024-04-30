from django.urls import path
from vendors.views import (
    VendorListCreateView,
    VendorDetailView,
    PurchaseOrderListCreateView,
    PurchaseOrderDetailView,
    VendorPerformanceView
)
# project_name/urls.py

from django.contrib import admin
  # Import include to include app-specific URLs




urlpatterns = [
     path('admin/', admin.site.urls),
    path('vendors/', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('vendors/<int:pk>/', VendorDetailView.as_view(), name='vendor-detail'),
    path('purchase_orders/', PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('purchase_orders/<int:pk>/', PurchaseOrderDetailView.as_view(), name='purchase-order-detail'),
    path('vendors/<int:pk>/performance/', VendorPerformanceView.as_view(), name='vendor-performance'),
]
