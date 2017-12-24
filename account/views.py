from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView
from account.forms import UserForm, UserProfileInfoForm, LoginForm
from account.models import UserProfileInfo


def userdetail(request):
    username = request.session['username']
    if username:
        userprofile = UserProfileInfo.objects.get(user=User(username='lunch'))
        # userprofile = UserProfileInfo.objects.get(address='aaa')
        return render(request, 'account/detail.html', {'object':userprofile})
    else:
        return redirect('/account/')


def index(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'account/loggedin.html', {'username': username})

    else:
        return redirect('/account/login/')


def register(request):
    """Register View"""
    if request.method == "POST":
        # check form validation
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            # save user_form to db
            user = user_form.save()
            # hash the password
            user.set_password(user.password)
            # update user
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            request.session['username'] = user.username
        else:
            print(user_form.errors, profile_form.errors)
        return redirect('/account/')
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        context_dir = {
            'title': "Register",
            'user_form': user_form,
            'profile_form': profile_form,
        }
    return render(request, 'account/register.html', context=context_dir)


def login(request):
    username = "not logged in"
    if request.method == "POST":
        # Get the posted form
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            request.session['username'] = username
            return redirect('/account/')
        else:
            raise login_form.ValidationError("User or password incorrect!")
    else:
        login_form = LoginForm()
        context_dict = {
            'title': "Login",
            'form': login_form,
        }
    return render(request, 'account/login.html', context_dict)


def logout(request):
    username = ""
    try:
        username = request.session['username']
        del request.session['username']
    except:
        pass
    return render(request, 'account/loggedout.html', {'username': username})
