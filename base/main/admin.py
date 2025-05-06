from django.contrib import admin
from main.models import Reviews, Order

admin.site.register(Reviews)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "service", "date", "time", "created_at")
    list_filter = ("service", "date")
    search_fields = ("name", "phone", "address")
