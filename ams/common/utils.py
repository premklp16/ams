import os
from django.forms import ValidationError


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.png', '.jpeg', '.JPG']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')