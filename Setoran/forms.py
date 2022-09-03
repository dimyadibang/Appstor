from django import forms
from django.forms import ModelForm, ModelChoiceField
from .models import Ustadz, Setoran, Kitab, Mahasantri

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UstadzForm(ModelForm):
    class Meta:
        model = Ustadz
        fields= '__all__'
        exclude = ['user']


class MahasantriForm(ModelForm):
    class Meta:
        model = Mahasantri
        fields = '__all__'


class SetoranForm(ModelForm):
    class Meta:
        model = Setoran
        fields = ('mahasantri', 'kitab')
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['kitab'].label = 'Pilih Kitab'


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UstadzForm(ModelForm):
    class Meta:
        model = Ustadz
        fields = '__all__'
        exclude = ['user']

