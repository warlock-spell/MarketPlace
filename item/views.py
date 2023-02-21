from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import NewItemForm, EditItemForm


# Create your views here.

def browse_items(request):
    items = Item.objects.filter(is_sold=False)
    context = {'items': items, }
    return render(request, 'item/browse-items.html', context)


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


@login_required
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard:dashboard')


@login_required
def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:item-detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })
