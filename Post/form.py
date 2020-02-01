from django import forms
from .models import Postlar

class YaratForm(forms.ModelForm):
    class Meta:
        model=Postlar
        fields={
            'basliq',
            'metin',
            'istifadeci',
            'sekil',
        }