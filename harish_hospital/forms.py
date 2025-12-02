from django import forms
from harish_hospital.models import CustomUser, Doctor, TimeSlot

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




# class BookingForm(forms.Form):
#     name = forms.CharField(
#         widget=forms.TextInput(attrs={"class": "form-control"}),
#         required=True
#     )

#     email = forms.EmailField(
#         widget=forms.EmailInput(attrs={"class": "form-control"}),
#         required=False
#     )

#     phone = forms.CharField(
#         widget=forms.TextInput(attrs={"class": "form-control"}),
#         required=True
#     )

#     department = forms.ModelChoiceField(
#         queryset=Doctor.objects.distinct('department'),
#         widget=forms.Select(attrs={"class": "form-control"}),
#         required=True
#     )

#     doctor = forms.ModelChoiceField(
#         queryset=CustomUser.objects.filter(role="doctor"),
#         widget=forms.Select(attrs={"class": "form-control"}),
#         required=True
#     )

#     timeslot = forms.ModelChoiceField(
#         queryset=TimeSlot.objects.filter(is_booked=False),
#         widget=forms.Select(attrs={"class": "form-control"}),
#         required=True
#     )
# class BookingForm(forms.Form):
#     name = forms.CharField(
#         widget=forms.TextInput(attrs={"class": "form-control"}),
#         required=True
#     )

#     email = forms.EmailField(
#         widget=forms.EmailInput(attrs={"class": "form-control"}),
#         required=False
#     )

#     phone = forms.CharField(
#         widget=forms.TextInput(attrs={"class": "form-control"}),
#         required=True
#     )

#     # Step 1 → department list (distinct)
#     department = forms.ModelChoiceField(
#         queryset=Doctor.objects.all().values_list("department", flat=True).distinct(),
#         widget=forms.Select(attrs={"class": "form-control"}),
#         required=True
#     )

#     # Step 2 → doctor list (initially empty)
#     doctor = forms.ModelChoiceField(
#         queryset=Doctor.objects.none(),
#         widget=forms.Select(attrs={"class": "form-control"}),
#         required=False
#     )

#     # Step 3 → timeslots (initially empty)
#     timeslot = forms.ModelChoiceField(
#         queryset=TimeSlot.objects.none(),
#         widget=forms.Select(attrs={"class": "form-control"}),
#         required=False
#     )

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         ### FILTER DOCTORS WHEN DEPARTMENT IS SELECTED ###
#         if "department" in self.data:
#             department_name = self.data.get("department")
#             self.fields["doctor"].queryset = Doctor.objects.filter(
#                 department=department_name,
#                 role="doctor"
#             )
#         else:
#             self.fields["doctor"].queryset = Doctor.objects.none()

#         ### FILTER TIMESLOTS WHEN DOCTOR IS SELECTED ###
#         if "doctor" in self.data:
#             doctor_id = self.data.get("doctor")
#             self.fields["timeslot"].queryset = TimeSlot.objects.filter(
#                 doctor_id=doctor_id,
#                 is_booked=False
#             )
#         else:
#             self.fields["timeslot"].queryset = TimeSlot.objects.none()


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
    
    description = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=False
    )

    # department list as choices
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
