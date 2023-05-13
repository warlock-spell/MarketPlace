from django.shortcuts import render, redirect
from item.models import Item, Category
from .forms import SignupForm

# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=False).order_by('-created_at')[0:6]
    categories = Category.objects.all()
    context = {'items': items, 'categories': categories}
    return render(request, 'core/index.html', context)


def contact(request):
    return render(request, 'core/contact.html')


def privacy_policy(request):
    return render(request, 'core/privacy-policy.html')


def terms(request):
    return render(request, 'core/terms.html')


def about(request):
    return render(request, 'core/about.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })