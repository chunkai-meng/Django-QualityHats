from django.shortcuts import render
from django.http import HttpResponse
from .models import Hat, Category, Supplier
from .forms import HatForm
# Create your views here.


def index(request):
    hat_list = Hat.objects.order_by('name')
    context_dir = {'hat_list': hat_list}
    return render(request, 'product_app/index.html', context=context_dir)


def add_hat(request):
    hat_form = HatForm()

    if request.method == "POST":
        hat_form = HatForm(request.POST, request.FILES)

        if hat_form.is_valid():
            hat = hat_form.save(commit=False)
            hat.category = Category.objects.get(id=request.POST['category'])
            hat.supplier = Supplier.objects.get(id=request.POST['supplier'])

            # if 'hat_pics' in request.FILES:
            #     hat.image = request.FILES['image']

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
