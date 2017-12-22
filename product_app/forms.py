from django import forms
from .models import Hat, Category, Supplier


class HatForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all())

    class Meta():
        model = Hat
        fields = ('name', 'description', 'price', 'image')
