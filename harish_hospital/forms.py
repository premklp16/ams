from django import forms
from harish_hospital.models import CustomUser, Doctor, TimeSlot


"""
Form classes for user registration, login, doctor registration,
and booking operations in the hospital management system.
"""

class UserRegisterForm(forms.ModelForm):
    """
    Form for registering new patients
    """
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Password"
        })
    )
    class Meta:
        model = CustomUser
        fields = ["name", "email", "phone_number", "password"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Full Name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone Number"}),
        }


class UserLoginForm(forms.Form):
    """
    Form for user login
    """
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Phone Number"
        })
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Password"
        })
    )


class BookingForm(forms.Form):
    """
    Form for booking an appointment
    """
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control"}),
        required=False
    )

    phone = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True
    )
    
    description = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=False
    )

    department = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True
    )

    doctor = forms.ModelChoiceField(
        queryset=Doctor.objects.none(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True
    )
    
    date = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control"}),
        required=True
    )

    timeslot = forms.ModelChoiceField(
        queryset=TimeSlot.objects.none(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True
    )


class DoctorRegisterForm(forms.ModelForm):
    """
    Form for admin to register a doctor
    """
    class Meta:
        model = Doctor
        fields = ["name", "email", "phone_number", "password", "department", "description", "experience", "education"]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Full Name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone Number"}),
            "password": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}),
            "department": forms.TextInput(attrs={"class": "form-control", "placeholder": "Department"}),
            "description": forms.TextInput(attrs={"class": "form-control", "placeholder": "Description"}),
            "experience": forms.TextInput(attrs={"class": "form-control", "placeholder": "Experience"}),
            "education": forms.TextInput(attrs={"class": "form-control", "placeholder": "Education"}),
        }

