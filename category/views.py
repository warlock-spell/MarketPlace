from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Category
from item.models import Item


def category_detail(request, slug_received):
    category = get_object_or_404(Category, slug=slug_received)
    categories = Category.objects.all()
    all_items = Item.objects.filter(category=category, is_sold=False)
    print(all_items)
    context = {
        "selected_category": category,
        "items": all_items,
        "categories": categories,
    }
    return render(request, "category/category-detail.html", context)
