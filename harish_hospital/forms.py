from django import forms
from harish_hospital.models import CustomUser, TimeSlot

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Password"
        })
    )

    class Meta:
        model = CustomUser
        fields = ["name", "email", "phone_number", "role", "password"]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Full Name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone Number"}),
            "role": forms.Select(attrs={"class": "form-control"}, choices=[
                ("patient", "Patient"),
                ("doctor", "Doctor"),
            ]),
        }

class UserLoginForm(forms.Form):
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

DEPARTMENT_CHOICES = [
    ("Cardiology", "Cardiology"),
    ("ENT", "ENT"),
    ("General Medicine", "General Medicine"),
    ("Orthopedics", "Orthopedics"),
]


class BookingForm(forms.Form):
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

    department = forms.ChoiceField(
        choices=DEPARTMENT_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True
    )

    doctor = forms.ModelChoiceField(
        queryset=CustomUser.objects.filter(role="doctor"),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True
    )

    timeslot = forms.ModelChoiceField(
        queryset=TimeSlot.objects.filter(is_booked=False),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True
    )