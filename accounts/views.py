from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import Group


def register_view(request: HttpRequest):
    form = UserCreationForm(request.POST or None)

    if request.method == 'POST':
        driver_reg_qp = request.POST["driver_reg"]

        is_driver_reg = False
        if driver_reg_qp is not None:
            is_driver_reg = bool(int(driver_reg_qp))

        if form.is_valid():
            user = form.save()
            if is_driver_reg:
                (drivers_group, error) = Group.objects.get_or_create(name='drivers')
                drivers_group.user_set.add(user)

            login(request, user)
            return redirect('index')

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = AuthenticationForm(data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')
