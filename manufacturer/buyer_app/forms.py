from django import forms
from .models import FileUpload

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['file', 'manufacturing_method', 'material', 'nozzle_dia', 'resolution', 'infill', 'layers']

    def __init__(self, *args, **kwargs):
        super(FileUploadForm, self).__init__(*args, **kwargs)
        self.fields['material'].required = False
        self.fields['nozzle_dia'].required = False
        self.fields['resolution'].required = False
        self.fields['infill'].required = False
        self.fields['layers'].required = False

        if self.is_bound and 'manufacturing_method' in self.data:
            method = self.data.get('manufacturing_method')
            self.adjust_fields(method)
        elif self.instance.pk:
            self.adjust_fields(self.instance.manufacturing_method)

    def adjust_fields(self, method):
        if method == '3d_printing':
            self.fields['material'].required = True
            self.fields['nozzle_dia'].required = True
            self.fields['resolution'].required = True
            self.fields['infill'].required = True
        elif method == 'cnc_machining':
            self.fields['material'].required = True
        elif method == 'pcb_manufacturing':
            self.fields['layers'].required = True
