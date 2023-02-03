from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Item


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    # fetching related items excluding the current item
    related_items = Item.objects.filter(
        category=item.category, is_sold=False
    ).exclude(pk=pk)[:3]
    context = {'item': item, 'related_items': related_items, }
    return render(request, 'item/item-detail.html', context)
