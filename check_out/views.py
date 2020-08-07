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
    }

    return render(request, template, context)
