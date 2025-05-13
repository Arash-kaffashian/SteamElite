from django.shortcuts import render, redirect
from user.templates.user.forms import CreateUserForm, AccountForm, LoginForm, UpdateUserForm, UpdateAccountForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Account


def register(request):
    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        account_form = AccountForm(request.POST)

        if user_form.is_valid() and account_form.is_valid():
            user = user_form.save()
            account = account_form.save(commit=False)
            account.user = user
            account.save()
            return redirect("my-login")
    else:
        user_form = CreateUserForm()
        account_form = AccountForm()

    context = {'registerform': user_form, 'accountform': account_form}

    return render(request, 'user/register.html', context=context)


def my_login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                login(request, user)
                messages.success(request, 'you have been logged in!')
                return redirect("dashboard")

    context = {'loginform': form}

    return render(request, 'user/my-login.html', context=context)


def my_logout(request):
    logout(request)
    messages.success(request, 'you have been logged out!')
    return redirect('home')


def dashboard(request):

    return render(request, 'user/dashboard.html')


def user_update(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        current_account = Account.objects.get(user=request.user)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)
        account_form = UpdateAccountForm(request.POST or None, instance=current_account)

        if user_form.is_valid() and account_form.is_valid():
            user_form.save()
            account_form.save()

            login(request, current_user)
            messages.success(request, 'Profile updated successfully!!!')
            return redirect('home')
        return render(request, 'user/user_update.html', {'user_form': user_form, 'account_form': account_form})
    else:
        messages.success(request, 'you have to logged in first to access this page!!!')
        return redirect('home')
