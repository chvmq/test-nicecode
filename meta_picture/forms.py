from django import forms

from .models import Image


class UploadImageForm(forms.ModelForm):
    title = forms.CharField(
        label='Пикча',
        widget=forms.TextInput(attrs={"class": 'form-control'})
    )

    image = forms.FileField(
        label='image')

    class Meta:
        model = Image
        fields = ('title', 'image')
