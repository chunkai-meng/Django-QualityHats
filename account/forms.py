from django import forms
from django.contrib.auth.models import User
from account.models import UserProfileInfo

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_message(self):
        username = self.cleaned_data.get("username")
        dbuser = User.objects.filter(name=username)
        if not dbuser:
            raise forms.ValidationError("User does not exist in our database!")
        return username


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ['username', 'email', 'password']
        help_texts = {
            'username': '',
        }



class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ['phone', 'address']
        labels = {
            'phone': "Phone Number",
            'address': "Address",
        }
