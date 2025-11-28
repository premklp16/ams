from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from ams.common.utils import create_or_edit_item
from harish_hospital.forms import UserRegisterForm
from harish_hospital.models import Booking, CustomUser, TimeSlot
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import BookingForm, UserLoginForm


@login_required
def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')

@login_required
def admin_doctors(request):
    doctors = CustomUser.objects.filter(role='doctor')
    return render(request, 'admin/doctors.html', {"doctors": doctors})


@login_required
def admin_patients(request):
    patients = CustomUser.objects.filter(role='patient')
    return render(request, 'admin/patients.html', {"patients": patients})

@login_required
def admin_add_doctor(request, pk=None):
    return create_or_edit_item(request, CustomUser, UserRegisterForm, 'admin/add_doctor.html', pk,
                               'admin_doctors')
