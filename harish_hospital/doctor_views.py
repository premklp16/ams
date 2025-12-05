from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import redirect, render
from harish_hospital.forms import UserLoginForm
from harish_hospital.models import Booking, Doctor, TimeSlot
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from datetime import date, datetime


# -------------------------------------- DOCTOR VIEWS -----------------------------------------

def doctor_get_login(request):
    """
    Authenticate doctor using phone number and password
    
    POST:
        - Validate form
        - Authenticate doctor (user)
        - Redirect to doctor dashboard
    
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
                if user.role == "doctor":
                    return redirect("doctor_dashboard")

            else:
                messages.error(request, "Invalid phone number or password")
                return render(request, "doctor_login.html", {"form": form, "message" : "Invalid phone number or password"})

    else:
        form = UserLoginForm()
        print("first")

    return render(request, "doctor_login.html", {"form": form})


@login_required
def doctor_dashboard(request):
    """
    Displays doctor's upcoming appointments and appointments today
    """
    try:
        doctor = Doctor.objects.get(id=request.user.id)
    except Doctor.DoesNotExist:
        return redirect('login_user')

    bookings = Booking.objects.filter(doctor=doctor).select_related("patient", "timeslot")
    today_slots = list(TimeSlot.objects.filter(date=date.today(), doctor=doctor))
    today_slots.sort(key=lambda x: datetime.strptime(x.time, "%I:%M %p"))

    return render(request, "doctor/dashboard.html", {
        "doctor": doctor,
        "bookings": bookings,
        "todays_slots": today_slots,
    })


@login_required
def doctor_profile(request):
    """
    Displays doctor profile
    """
    doctor = Doctor.objects.get(id=request.user.id)
    return render(request, "doctor/doctor_profile.html", {"doctor": doctor})

