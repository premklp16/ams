from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from ams.common.utils import create_or_edit_item
from harish_hospital.forms import DoctorRegisterForm
from harish_hospital.models import CustomUser, Doctor



@login_required
def admin_dashboard(request):
    doctor_count = CustomUser.objects.filter(role="doctor").count
    patient_count = CustomUser.objects.filter(role="patient").count
    admin = request.user
    return render(request, 'admin/dashboard.html', {"doc_count":doctor_count, "pat_count" : patient_count, "admin" : admin})

@login_required
def admin_doctors(request):
    doctors = Doctor.objects.filter(role='doctor')
    return render(request, 'admin/doctors.html', {"doctors": doctors})


@login_required
def admin_patients(request):
    patients = CustomUser.objects.filter(role='patient')
    return render(request, 'admin/patients.html', {"patients": patients})

@login_required
def admin_add_doctor(request, pk=None):
    return create_or_edit_item(request, Doctor, DoctorRegisterForm, 'admin/add_doctor.html', 'doctor', pk,
                               'admin_doctors')
