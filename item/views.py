from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import NewItemForm


# Create your views here.

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    # fetching related items excluding the current item
    related_items = Item.objects.filter(
        category=item.category, is_sold=False
    ).exclude(pk=pk)[:3]
    context = {'item': item, 'related_items': related_items, }
    return render(request, 'item/item-detail.html', context)


@login_required
def new_item(request):
    if request.method == 'POST':
        # request.files is used to get the image
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:item-detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })
