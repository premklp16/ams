from django.shortcuts import redirect, render
from harish_hospital.models import Booking, Doctor
from django.contrib.auth.decorators import login_required

@login_required
def doctor_dashboard(request):
    try:
        doctor = Doctor.objects.get(id=request.user.id)
    except Doctor.DoesNotExist:
        return redirect('login_user')

    # All bookings for this doctor
    bookings = Booking.objects.filter(doctor=doctor).select_related("patient", "timeslot")

    return render(request, "doctor/dashboard.html", {
        "doctor": doctor,
        "bookings": bookings
    })

@login_required
def doctor_profile(request):
    doctor = Doctor.objects.get(id=request.user.id)
    return render(request, "doctor/doctor_profile.html", {"doctor": doctor})