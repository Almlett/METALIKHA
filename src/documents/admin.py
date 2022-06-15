from django.contrib import admin
from documents.models import Quote, QuoteItem

class QuoteAdmin(admin.ModelAdmin):
    pass

class QuoteItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Quote, QuoteAdmin)
admin.site.register(QuoteItem, QuoteItemAdmin)