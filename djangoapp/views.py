from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import MenuForm
from .forms import AddForm
from .forms import RemoveForm
# from .forms import RemoveForm
# from .forms import Checkout
from .store import Store
from django.shortcuts import redirect

store = Store()


# Create your views here.
def main_menu(request):

    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            choice = int(form.cleaned_data['options'])
            if choice is 1:
                return redirect(print_store)
            if choice is 2:
                return redirect(print_cart)
            if choice is 3:
                return redirect(add_items)
            if choice is 4:
                return redirect(remove_items)
            if choice is 5:
                return redirect(checkout)

            return redirect()
    else:
        form = MenuForm()

    return render(request, 'main_menu.html', {'form': form})


def print_store(request):
    items = store.items
    return render(request, 'pstore.html', {'items': items})


def print_cart(request):
    items = store.get_cart_items()
    cart_list = []

    for item in items:
        cart_item = str(item.name) + ": " + str(item.description) + " $" + str(item.price) + " (" + \
                     str(store.get_cart_item_qty(item)) + ")"
        cart_list.append(cart_item)

    return render(request, 'pcart.html', {'cart_list': cart_list})


def add_items(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            choice = int(form.cleaned_data['items'])
            qty = form.cleaned_data['quantity']
            if choice is 1:
                store.add_to_cart(store.items[0], qty)
                return redirect(main_menu)
            if choice is 2:
                store.add_to_cart(store.items[1], qty)
                return redirect(main_menu)
            if choice is 3:
                store.add_to_cart(store.items[2], qty)
                return redirect(main_menu)
            if choice is 4:
                store.add_to_cart(store.items[3], qty)
                return redirect(main_menu)

            return redirect()
    else:
        form = AddForm()

    return render(request, 'addCart.html', {'form': form})


def remove_items(request):
    if request.method == 'POST':
        form = RemoveForm(request.POST)
        if form.is_valid():
            choice = int(form.cleaned_data['items'])
            qty = form.cleaned_data['quantity']
            if choice is 1:
                store.remove_from_cart(store.items[0], qty)
                return redirect(main_menu)
            if choice is 2:
                store.remove_from_cart(store.items[1], qty)
                return redirect(main_menu)
            if choice is 3:
                store.remove_from_cart(store.items[2], qty)
                return redirect(main_menu)
            if choice is 4:
                store.remove_from_cart(store.items[3], qty)
                return redirect(main_menu)

            return redirect()
    else:
        form = RemoveForm()

    return render(request, 'removeCart.html', {'form': form})


def checkout(request):
    items = store.get_cart_items()
    cart_list = []
    grand_total = 0

    for item in items:
        cart_item = str(item.name) + ": " + str(item.description) + " $" + str(item.price) + " (" + \
                    str(store.get_cart_item_qty(item)) + ") Total Price: " + str(store.total_price(item))
        cart_list.append(cart_item)
        grand_total += store.total_price(item)
    return render(request, 'checkout.html', {'cart_list': cart_list, 'grand_total': grand_total})
