from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def check_out(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'check_out/check_out.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HDWiQG4FS2lVNP2ZjAZuL3La3a4zsL9VwsrPPprns3YiMqaYQ5sV3tUWfhveQvE2p4jLaIYP39EZEoKxPQ3bxdU00Nqx8yy28',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
