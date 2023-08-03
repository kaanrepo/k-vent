from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field


class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ('username', 'email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise ValidationError("Passwords don't match.")
        return password2

    def save(self, commit=True):
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password',
                  'active', 'staff', 'superuser',)

        def clean_password(self):
            return self.initial['password']


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise ValidationError("Passwords don't match.")
        return password2


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Field('username', css_class='custom-font')
        )
