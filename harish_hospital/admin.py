from django.contrib import admin

from harish_hospital.models import Booking, CustomUser, TimeSlot

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Booking)
admin.site.register(TimeSlot)