from django import template

register = template.Library()

@register.filter
def count_unsold_items(queryset):
    return queryset.filter(is_sold=False).count()
