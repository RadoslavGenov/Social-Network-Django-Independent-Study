from django.core.files import File
from django import forms
import os
import urllib
from .models import Image


class ImageCreateForm(forms.ModelForm):

    def save(self, force_insert=False, force_update=False, commit=True):
        image = super(ImageCreateForm, self).save(commit=False)
        image_url = self.cleaned_data['url']

        result = urllib.urlretrieve(image_url)
        image.image.save(
            os.path.basename(image_url),
            File(open(result[0])),
            save=False
        )

        if commit:
            image.save()
        return image

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('The given url does not match valid image extensions!')
        return url

    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        widgets = {
            'url': forms.HiddenInput,
        }