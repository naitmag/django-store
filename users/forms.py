from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Имя пользователя:",
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "class": "form-control",
                "placeholder": "Введите имя пользователя"
            }
        )
    )
    password = forms.CharField(
        label="Пароль:",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "class": "form-control",
                "placeholder": "Введите пароль"
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'password']
