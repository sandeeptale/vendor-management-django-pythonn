# vendors/admin.py

from django.contrib import admin
from .models import Vendor, PurchaseOrder

# Register Vendor model
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'vendor_code', 'address', 'contact_details']
    search_fields = ['name', 'vendor_code']  # Enable search by name or vendor code

# Register PurchaseOrder model
@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ['po_number', 'vendor', 'order_date', 'delivery_date', 'status']
    list_filter = ['status']  # Add filter by status
    search_fields = ['po_number', 'vendor__name']  # Enable search by PO number or vendor name
