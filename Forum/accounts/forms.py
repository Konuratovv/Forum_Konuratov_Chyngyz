from django import forms
from django.contrib.auth.models import User

from accounts.models import Profile


class RegisterForm(forms.ModelForm):
    username = forms.CharField(label="username", required=True)
    password = forms.CharField(label="password", strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="confirm_password", strip=False, required=True, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')
        if not username:
            raise forms.ValidationError("Enter username")
        if not password:
            raise forms.ValidationError('Enter password')
        if not password_confirm:
            raise forms.ValidationError('Enter this field')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']

