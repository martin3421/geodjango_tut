from django import forms


class UploadGpxForm(forms.Form):
    gpx_file = forms.FileField(label='Select a file')