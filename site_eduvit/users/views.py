from datetime import datetime
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import AuthUserForm, UserRegistrationForm, UserCreationForm


class Login(LoginView):
    fields = ["username", "password"]
    template_name = 'users/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('mysite:index')

class Logout(LogoutView):
    next_page = reverse_lazy('mysite:index')



def register(request):
    regform = UserRegistrationForm(request.POST)
    if request.method == "POST":
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_active = True
            reg_f.is_staff = False
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()
            regform.save()

            reg_f.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, reg_f)
            return redirect('mysite:index')
    else:
        regform = UserCreationForm()
    return render(request, 'users/register.html', {"regform": regform})