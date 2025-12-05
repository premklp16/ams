from datetime import date
from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from ams.common.utils import create_or_edit_item
from harish_hospital.forms import DoctorRegisterForm, UserLoginForm
from harish_hospital.models import CustomUser, Doctor, TimeSlot


# ---------------------------------- ADMIN VIEWS -------------------------------------

def admin_get_login(request):
    """
    Authenticate admin using phone number and password
    
    POST:
        - Validate form
        - Authenticate admin (user)
        - Redirect to admin dashboard
    
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
                if user.role == "admin":
                    return redirect("admin_dashboard")

            else:
                messages.error(request, "Invalid phone number or password")
                return render(request, "admin_login.html",
                              {"form": form,
                                "msg" : "Invalid phone number or password"}
                              )

    else:
        form = UserLoginForm()
        print("first")

    return render(request, "admin_login.html", {"form": form})


@login_required
def admin_dashboard(request):
    """
    Display the admin dashboard with
        - Number of doctors currently working
        - Number of patients have registered
        - Number of appointments booked today
    """
    doctor_count = CustomUser.objects.filter(role="doctor").count
    patient_count = CustomUser.objects.filter(role="patient").count
    appointment_today = TimeSlot.objects.filter(date=date.today(), is_booked= True).count()
    admin = request.user
    return render(request,
                  'admin/dashboard.html',
                  {"doc_count":doctor_count,
                   "pat_count" : patient_count,
                   "admin" : admin,
                   "appointment_today":appointment_today,
                   "date" : date.today()}
                )

@login_required
def admin_doctors(request):
    """
    Displays doctors details
    """
    doctors = Doctor.objects.filter(role='doctor')
    return render(request, 'admin/doctors.html', {"doctors": doctors})


@login_required
def admin_patients(request):
    """
    Displays registered patient details
    """
    patients = CustomUser.objects.filter(role='patient')
    return render(request, 'admin/patients.html', {"patients": patients})


@login_required
def admin_add_doctor(request, pk=None):
    """
    Allows admin to add doctor
    """
    return create_or_edit_item(request, Doctor, DoctorRegisterForm, 'admin/add_doctor.html', 'doctor', pk,
                               'admin_doctors')


@login_required
def deactivate_doctor(request, id):
    """
    Allows admin to activate and deactivate doctors
    """
    doctor = get_object_or_404(CustomUser, id=id)
    doctor.is_active = not doctor.is_active
    doctor.save()
    return redirect('admin_doctors')

 