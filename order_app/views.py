from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from . import models
# Create your views here.


class OrderIndexView(View):
    template_name = 'index.html'


class OrderListView(ListView):
    model = models.Order


class OrderDetailView(DetailView):
    model = models.Order


class OrderCreateView(CreateView):
    fields = ('account', 'recipient', 'phone_number', 'street_line1',
              'street_line2', 'zipcode', 'city', 'state')
    model = models.Order


class OrderUpdateView(UpdateView):
    fields = ('account', 'recipient', 'phone_number', 'street_line1',
              'street_line2', 'zipcode', 'city', 'state')
    model = models.Order


class OrderDeleteView(DeleteView):
    model = models.Order
    success_url = reverse_lazy("order_app:list")

