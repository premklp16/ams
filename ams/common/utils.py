import os
from django.forms import ValidationError
from django.shortcuts import get_object_or_404, redirect, render


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.png', '.jpeg', '.JPG']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

def create_or_edit_item(request, model, form_class, template_name, pk=None, redirect_to=None):
    is_edit = pk is not None
    instance = get_object_or_404(model, pk=pk) if is_edit else None

    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            # form.save()
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect(redirect_to)
    else:
        form = form_class(instance=instance)
    return render(request, template_name, {'form': form, 'is_edit': is_edit})
