from django.contrib import admin
from .models import InventoryItem

# Register your models here.

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'unit', 'expiry_date', 'user', 'created_at']
    list_filter = ['expiry_date', 'created_at', 'unit']
    search_fields = ['name', 'user__username']
    ordering = ['-created_at']
