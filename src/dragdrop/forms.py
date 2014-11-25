from django import forms
from dragdrop.models import UploadFile

class UploadFileForm(forms.ModelForm):

    class Meta:
        model = UploadFile
        exclude = ('user',)