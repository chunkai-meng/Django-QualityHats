from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView
from . import models
from .forms import HatForm


def index(request):
    hat_list = models.Hat.objects.order_by('name')
    username = username = request.session['username'] if 'username' in request.session else ''
    context_dir = {
        'username': username,
        'hat_list': hat_list
    }
    return render(request, 'product_app/index.html', context=context_dir)


def add_hat(request):
    hat_form = HatForm()
    if request.method == "POST":
        hat_form = HatForm(request.POST, request.FILES)
        if hat_form.is_valid():
            hat = hat_form.save(commit=False)
            hat.category = models.Category.objects.get(id=request.POST['category'])
            hat.supplier = models.Supplier.objects.get(id=request.POST['supplier'])
            hat.save()
            print("Hat Added")
        else:
            print(hat_form.errors)
    else:
        hat_form = HatForm()
    return render(request, 'product_app/add_hat.html', {'hat_form': hat_form})


def test(request, year, month):
    text = "The number is %s/%s" % (month, year)
    return HttpResponse(text)
