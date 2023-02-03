from django.contrib import admin

# Register your models here.
from .models import Category, Item

admin.site.register(Category)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_sold', 'created_by', 'created_at')
    list_filter = ('is_sold', 'category', 'created_by')
    search_fields = ('name', 'description', 'category')
    readonly_fields = ('created_at',)


admin.site.register(Item, ItemAdmin)
