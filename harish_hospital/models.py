from datetime import timezone
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
import uuid
from django.core.validators import RegexValidator
from ams.common.utils import validate_file_extension


"""
Models for storing user details, doctor specific details, timeslot details, booking details
"""

class CustomUserManager(BaseUserManager):
    """
    Custom manager for creating users and superusers

    Methods:
    - create_user(): Creates a normal user with phone_number as username
    - create_superuser(): Creates admin with is_staff and is_superuser permissions
    """
    
    def create_user(self, phone_number, password=None, role='patient', **extra_fields):
        if not phone_number:
            raise ValueError('The phone_number field must be set')
        user = self.model(phone_number=phone_number, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone_number, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model replacing Django's default user
    
    - Uses phone_number as USERNAME_FIELD
    - Supports roles like 'patient' or 'doctor'
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_alpha_validator = RegexValidator(r'^[a-zA-Z]', message='name must be alphabet')
    name = models.CharField(max_length=30, blank=True, null=True, validators=[is_alpha_validator])
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{14,14}$',
                                 message="Phone number must be entered Up to 14 digits allowed")
    phone_number = models.CharField(max_length=10, unique=True)
    role = models.CharField(max_length=20, blank=True, null=True)
    street_address_1 = models.CharField(max_length=250, null=True, blank=True)
    street_address_2 = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=5, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_img/', validators=[validate_file_extension], null=True,
                                      blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_block = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    is_phone_number_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    last_login = models.DateTimeField(auto_now_add = True, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'users'

class Doctor(CustomUser):
    """
    Doctor model extends CustomUser
    
    Additional fields:
    - department: Doctor's specialization
    - description: Short bio
    - experience: Years of experience
    - education: Education background
    """
    department = models.CharField(max_length= 30)
    description = models.CharField(max_length= 100)
    experience = models.PositiveIntegerField(default=0)
    education = models.CharField(max_length= 30)

    def __str__(self):
        return self.department

class TimeSlot(models.Model):
    """
    Stores timeslot details for each doctor
    """
    doctor = models.ForeignKey(CustomUser, on_delete= models.CASCADE, limit_choices_to= {'role': 'doctor'})
    date = models.DateField()
    time = models.CharField(max_length=20)  
    is_booked = models.BooleanField(default=False)


class Booking(models.Model):
    """
    Stores an appointment booking details between doctor and patient
    """
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, unique=True, editable=False)
    patient = models.ForeignKey(CustomUser, on_delete= models.CASCADE, limit_choices_to= {'role':'patient'}, related_name='patient_bookings')
    doctor = models.ForeignKey(CustomUser, on_delete= models.CASCADE, limit_choices_to= {'role':'doctor'}, related_name='doctor_bookings')
    timeslot = models.ForeignKey(TimeSlot, on_delete= models.CASCADE)
    description = models.TextField(blank=True, null=True)
    
