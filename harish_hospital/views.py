from datetime import date
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from harish_hospital.forms import UserRegisterForm
from harish_hospital.models import Booking, Doctor, TimeSlot
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import BookingForm, UserLoginForm


# ---------------------------------- PUBLIC VIEWS ----------------------------------------------

def index(request):
    """
    Render the Home Page
    """
    return render(request, 'index.html')


def about_us(request):
    """
    Render the About Us Page
    """
    return render(request, 'aboutus.html')


def department(request):
    """
    Render the Department Details Page
    """
    return render(request,'department.html')


def health_packages(request):
    """
    Render the Available Health Packages Page
    """
    return render(request, 'health_packages.html')


def register(request):
    """
    Handle patient registeration
    
    POST:
        - Validate form
        - Save user details
        - Redirect to login
    
    GET:
        - Display registeration form
    """
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.role = 'patient'
            user.save()
            messages.success(request, "Registration successful!")
            return redirect("get_login")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserRegisterForm()
    return render(request, "patient/register.html", {"form": form})


def get_login(request):
    """
    Authenticate patient using phone number and password
    
    POST:
        - Validate form
        - Authenticate patient (user)
        - Redirect to patient dashboard
    
    GET:
        - Display login form
    """
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']

            user = authenticate(request, username=phone, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                if user.role == "patient":
                    return redirect("patient_dashboard")

            else:
                messages.error(request, "Invalid phone number or password")
                return render(request, "login.html",
                              {"form": form, "message" : "Invalid phone number or password"}
                            )

    else:
        form = UserLoginForm()

    return render(request, "login.html", {"form": form})


@login_required
def patient_dashboard(request):
    """
    Display the patient dashboard with
        - Available department and doctor related to department
        - Timeslots for today and future 
    
    POST:
        - Validate booking form
        - Mark selected timeslot as booked
        - Create booking object
        - Redirect booking success
    """
    doctors = Doctor.objects.filter(is_active=True)
    timeslots = TimeSlot.objects.filter(date__gte=date.today())

    departments = Doctor.objects.values_list("department", flat=True).distinct()
    department_choices = [(d, d) for d in departments]

    form = BookingForm()
    form.fields["department"].choices = department_choices

    form.fields["doctor"].queryset = doctors
    form.fields["timeslot"].queryset = timeslots

    if request.method == "POST":
        form = BookingForm(request.POST)
        form.fields["department"].choices = department_choices
        form.fields["doctor"].queryset = doctors
        form.fields["timeslot"].queryset = timeslots
        if form.is_valid():
            doctor = form.cleaned_data["doctor"]
            slot = form.cleaned_data["timeslot"]
            description=form.cleaned_data["description"]
            
            slot.is_booked = True
            slot.save()

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
    

@login_required
def booking_success(request, bookid):
    """
    Display the booking details

    Args:
        bookid (uuid): To access the booking details
    """
    book = Booking.objects.get(id=bookid)
    return render(request, "patient/booking_success.html", {"book": book})


@login_required
def logout_user(request):
    """
    Logout the current user
    """
    logout(request)
    return redirect('index')

