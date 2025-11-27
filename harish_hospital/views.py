from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.decorators import login_required

from harish_hospital.forms import UserRegisterForm
from harish_hospital.models import Booking, CustomUser, TimeSlot

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
            return redirect("user_login")
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
from .forms import BookingForm, UserLoginForm

def user_login(request):
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

@login_required
def patient_dashboard(request):
    if request.method == "POST":
        doctors = CustomUser.objects.filter(role="doctor")
        form = BookingForm(request.POST)

        if form.is_valid():
            doctor_id = form.cleaned_data["doctor"]
            timeslot_id = form.cleaned_data["timeslot"]
            description = form.cleaned_data["description"]

            if not doctor_id or not timeslot_id:
                messages.error(request, "Please select doctor and timeslot.")
                return redirect("book_appointment")

            doctor = get_object_or_404(CustomUser, id=doctor_id, role="doctor")
            timeslot = get_object_or_404(TimeSlot, id=timeslot_id, doctor=doctor)

            # Check if slot already booked
            if timeslot.is_booked:
                messages.error(request, "This timeslot is already booked.")
                return redirect("register")

            # Create booking
            Booking.objects.create(
                patient=request.user,   # logged-in patient
                doctor=doctor,
                timeslot=timeslot,
                description=description
            )

            # Mark timeslot as booked
            timeslot.is_booked = True
            timeslot.save()

            messages.success(request, "Appointment booked successfully!")
            return redirect("user_login")

    else:
        form = BookingForm()
    return render(request, "patient_dashboard.html", {"form": form})










