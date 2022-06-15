from django.contrib import admin
from documents.models import Quote, QuoteItem, PurchaseOrder, PurchaseOrderItem


class QuoteItemAdmin(admin.TabularInline):
    model = QuoteItem


class QuoteAdmin(admin.ModelAdmin):
    inlines = [QuoteItemAdmin]


class PurchaseOrderItemAdmin(admin.TabularInline):
    model = PurchaseOrderItem


class PurchaseOrderAdmin(admin.ModelAdmin):
    inlines = [PurchaseOrderItemAdmin]


admin.site.register(Quote, QuoteAdmin)
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
