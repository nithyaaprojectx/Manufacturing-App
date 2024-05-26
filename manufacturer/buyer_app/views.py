import os
import re
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FileUploadForm
from .models import FileUpload

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.core.files.storage import default_storage


@csrf_exempt
def upload_step_file(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if 'file' in request.FILES:
                file = request.FILES['file']
                file_name = default_storage.save(file.name, file)
                # You can save the file path to your model or perform further processing here
                return JsonResponse({'message': 'File uploaded successfully'}, status=200)
            else:
                return JsonResponse({'error': 'No file provided'}, status=400)
        else:
            return JsonResponse({'error': 'Authentication failed'}, status=401)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_upload = form.save(commit=False)
            file_upload.buyer = request.user.buyer
            file_upload.save()

            # Process the uploaded file to calculate the bounding box dimensions
            file_path = file_upload.file.path
            bounding_box = parse_gcode(file_path)

            return render(request, 'buyer/success.html', {
                'bounding_box': bounding_box,
                'file_upload': file_upload
            })
    else:
        form = FileUploadForm()
    return render(request, 'buyer/upload.html', {'form': form})

def parse_gcode(file_path):
    coord_pattern = re.compile(r'([XYZ])([-+]?\d*\.?\d+)')
    min_x = min_y = min_z = float('inf')
    max_x = max_y = max_z = float('-inf')

    with open(file_path, 'r') as file:
        for line in file:
            coords = coord_pattern.findall(line)
            if coords:
                for axis, value in coords:
                    value = float(value)
                    if axis == 'X':
                        min_x = min(min_x, value)
                        max_x = max(max_x, value)
                    elif axis == 'Y':
                        min_y = min(min_y, value)
                        max_y = max(max_y, value)
                    elif axis == 'Z':
                        min_z = min(min_z, value)
                        max_z = max(max_z, value)

    bounding_box = {
        'min_x': min_x,
        'max_x': max_x,
        'min_y': min_y,
        'max_y': max_y,
        'min_z': min_z,
        'max_z': max_z,
        'width': max_x - min_x,
        'depth': max_y - min_y,
        'height': max_z
    }

    return bounding_box


@login_required
def success(request):
    return render(request, 'buyer/success.html')
