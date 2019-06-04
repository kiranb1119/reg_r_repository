from django.shortcuts import render
from django.http.response import HttpResponse
from .models import RegistrationData
from .forms import RegForm, LoginForm


def reg_view(request):
    if request.method == 'POST':
        rform = RegForm(request.POST)
        if rform.is_valid():
            first_name = request.POST.get('first_name', '')
            last_name = request.POST.get('last_name', '')
            user_name = request.POST.get('username', '')
            password = request.POST.get('password', '')
            mobile = request.POST.get('mobile', '')
            email = request.POST.get('email', '')

            data = RegistrationData(
                first_name=first_name,
                last_name=last_name,
                username=user_name,
                password=password,
                mobile=mobile,
                email=email
            )
            data.save()
            lform = LoginForm()
            return render(request, 'loginform.html', {'lform': lform})
        else:
            return HttpResponse('invalid data')
    else:
        rform = RegForm()
        return render(request, 'reg_form.html', {'rform': rform})


def login_view(request):
    if request.method == 'POST':
        lform = LoginForm(request.POST)
        if lform.is_valid():
            uname = request.POST.get('uname', '')
            pwd = request.POST.get('pwd', '')
            uname1 = RegistrationData.objects.filter(username=uname)
            pwd1 = RegistrationData.objects.filter(password=pwd)
            if uname1 and pwd1:
                return HttpResponse('Correct username and password')
            else:
                return HttpResponse('invalid username and password')
        else:
            return HttpResponse('invalid data')
    else:
        lform = LoginForm()
        return render(request, 'loginform.html', {'lform': lform})