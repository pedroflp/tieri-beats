from django import forms
from .models import Header, Alert, Genre, Music, PriceCard

class HeaderForm(forms.ModelForm):
    exibir = forms.BooleanField()

    class Meta:
        model = Header
        fields = ['title', 'header']

    def __init__(self, *args, **kwargs):
        super(Header, self).__init__(*args, **kwargs)
        if check_something():
            self.fields['exibir'].initial  = True

class AlertForm (forms.ModelForm):
    exibir = forms.BooleanField()

    class Meta:
        model = Alert
        fields = ['h1', 'span']

    def __init__(self, *args, **kwargs):
        super(Alert, self).__init__(*args, **kwargs)
        if check_something():
            self.fields['exibir'].initial  = True

class GenreForm (forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(Genre, self).__init__(*args, **kwargs)


class MusicForm (forms.ModelForm):
    class Meta:
        model = Music
        fields = ['title', 'image', 'genre', 'audio', 'youtube', 'spotify', 'price']

    def __init__(self, *args, **kwargs):
        super(Music, self).__init__(*args, **kwargs)


class PriceCardForm (forms.ModelForm):
    class Meta:
        model = PriceCard
        fields = ['title', 'audiostream', 'audiocopies', 'soundformat', 'price', 'saleprice', 'buylink']

    def __init__(self, *args, **kwargs):
        super(CardPrice, self).__init__(*args, **kwargs)
        if check_something():
            self.fields['exibir'].initial  = True