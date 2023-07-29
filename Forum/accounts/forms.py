from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label="email", required=True)
    name = forms.CharField(label="name", required=False)
    username = forms.CharField(label="username", required=True)
    password = forms.CharField(label="password", strip=False, required=True, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        name = cleaned_data.get("name")
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if not email:
            raise forms.ValidationError("Enter email field")
        if not username:
            raise forms.ValidationError("Enter username")
        if not password:
            raise forms.ValidationError('Enter password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.email = self.cleaned_data["email"]
        user.save()
        return user

    class Meta:
        model = User
        fields = ['email', 'name', 'username', 'password']


class LoginForm(forms.ModelForm):
    email = forms.EmailField(label='email', max_length=30, required=True)
    password = forms.CharField(label="password", strip=False, required=True, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if not email:
            raise forms.ValidationError("Enter email")
        if not password:
            raise forms.ValidationError('Enter password')

    class Meta:
        model = User
        fields = ['email', 'password']
