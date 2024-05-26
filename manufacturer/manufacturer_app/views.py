from django.shortcuts import render, redirect
from .models import Manufacturer
from .forms import ManufacturerForm

def manufacturer_list(request):
    manufacturers = Manufacturer.objects.all()
    return render(request, 'manufacturer_app/manufacturer_list.html', {'manufacturers': manufacturers})

def manufacturer_create(request):
    if request.method == 'POST':
        form = ManufacturerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manufacturer_list')
    else:
        form = ManufacturerForm()
    return render(request, 'manufacturer_app/manufacturer_form.html', {'form': form})
