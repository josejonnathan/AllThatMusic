from django import forms
from .models import Artist, Song
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field


class ArtistUpdateForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['review', 'instagram_link', 'youtube_link']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Field('review', css_class='form-control mb-3'),
            Field('instagram_link', css_class='form-control bg-dark text-light mt-2'),
            Field('youtube_link', css_class='form-control bg-dark text-light mt-2'),
        )


class SongUpdateForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['lyrics', 'youtube_link']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Field('lyrics', css_class='form-control mb-3'),
            Field('youtube_link', css_class='form-control bg-dark text-light mt-2'),
        )
