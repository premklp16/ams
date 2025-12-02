from datetime import date, timedelta
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from harish_hospital.forms import UserRegisterForm
from harish_hospital.models import Booking, CustomUser, Doctor, TimeSlot
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import BookingForm, UserLoginForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'aboutus.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Registration successful!")
            return redirect("login")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {"form": form})

def get_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']

            # Authenticate using phone number
            user = authenticate(request, username=phone, password=password)
            if user is not None:
                login(request, user)
                print("user", user.role)
                messages.success(request, "Login successful!")
                if user.role == "doctor":
                    return redirect("doctor_dashboard")
                elif user.role == "patient":
                    return redirect("patient_dashboard")
                else:
                    return redirect("admin_dashboard")

                # return render(request, 'role_selection.html') # change to your homepage
            else:
                messages.error(request, "Invalid phone number or password")
                return render(request, "login.html", {"form": form})

    else:
        form = UserLoginForm()
        print("first")

    return render(request, "login.html", {"form": form})



@login_required
def patient_dashboard(request):
    doctors = Doctor.objects.all()
    timeslots = TimeSlot.objects.all()

    # Prepare department choices
    departments = Doctor.objects.values_list("department", flat=True).distinct()
    department_choices = [(d, d) for d in departments]

    form = BookingForm()
    form.fields["department"].choices = department_choices

    # IMPORTANT FIX: load all doctors and timeslots into form for JS filtering
    form.fields["doctor"].queryset = doctors
    form.fields["timeslot"].queryset = timeslots

    if request.method == "POST":
        form = BookingForm(request.POST)
        form.fields["department"].choices = department_choices
        form.fields["doctor"].queryset = doctors
        form.fields["timeslot"].queryset = timeslots
        print("Form errors:", form.errors)
        if form.is_valid():
            doctor = form.cleaned_data["doctor"]
            slot = form.cleaned_data["timeslot"]
            description=form.cleaned_data["description"]

            # Mark slot booked
            slot.is_booked = True
            slot.save()

            # Save booking
            book_obj = Booking.objects.create(
                patient=request.user,
                doctor=doctor,
                timeslot=slot,
                description=description,
            )
            return redirect("booking_success", bookid=book_obj.id)

    return render(request, "patient/dashboard.html", {
        "form": form,
        "doctors": doctors,
        "timeslots": timeslots,
    })

def booking_success(request, bookid):
    book = Booking.objects.get(id=bookid)
    return render(request, "patient/booking_success.html", {"book": book})

def logout_user(request):
    logout(request)
    return redirect('index')






