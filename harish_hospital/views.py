from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import check_password, make_password

from harish_hospital.forms import UserRegisterForm
from harish_hospital.models import CustomUser

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            
        # if form.is_valid():
        #     form.save()
            messages.success(request, "Registration successful!")
            return redirect("login_user")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserRegisterForm()
    return render(request, "patient_register.html", {"form": form})

# def register(request):
#     if request.method == "POST":
#         role = request.POST['role']   # P or D
#         name = request.POST['name']
#         age = request.POST['age']
#         gender = request.POST['gender']
#         phone = request.POST['phone']
#         email = request.POST['email']
#         password = make_password(request.POST['password'])
#         description = request.POST.get('description', "")
#         department = request.POST.get('department', "")

#         CustomUser.objects.create(
#             role=role,
#             name=name,
#             age=age,
#             gender=gender,
#             phone=phone,
#             email=email,
#             password=password,
#             description=description,
#             department=department
#         )

#         return redirect("login")

#     return render(request, "register.html")

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserLoginForm

def login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)

        if form.is_valid():
            phone = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']

            # Authenticate using phone number
            user = authenticate(request, username=phone, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return render(request, 'role_selection.html') # change to your homepage
            else:
                messages.error(request, "Invalid phone number or password")
                return render(request, "patient_login.html", {"form": form})

    else:
        form = UserLoginForm()

    return render(request, "patient_login.html", {"form": form})










