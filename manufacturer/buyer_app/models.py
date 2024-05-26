from django.db import models
from django.contrib.auth.models import User

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='buyer')
    name = models.CharField(max_length=255)  # Add a name field

    def __str__(self):
        return self.name


class FileUpload(models.Model):
    MANUFACTURING_METHOD_CHOICES = [
        ('3d_printing', '3D Printing'),
        ('cnc_machining', 'CNC Machining'),
        ('pcb_manufacturing', 'PCB Manufacturing'),
    ]

    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='uploads')
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    manufacturing_method = models.CharField(max_length=20, choices=MANUFACTURING_METHOD_CHOICES)
    material = models.CharField(max_length=100, blank=True, null=True)
    nozzle_dia = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    resolution = models.CharField(max_length=50, blank=True, null=True)
    infill = models.CharField(max_length=50, blank=True, null=True)
    layers = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.buyer.name} - {self.file.name} ({self.get_manufacturing_method_display()})"
