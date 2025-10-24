from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import PasswordResetForm as DjangoPasswordResetForm
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")


class PasswordResetForm(DjangoPasswordResetForm):
    email = forms.EmailField(label="Email")


User = get_user_model()


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'avatar')


class DepositForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2, min_value=1, label="Сумма пополнения")


class WithdrawForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2, min_value=1, label="Сумма вывода")



class OTPForm(forms.Form):
    code = forms.CharField(
            label='Код из почты', 
            max_length=6, 
            widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите 6-значный код'
                })
            )


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'avatar']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя пользователя'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+996 700 123 456'
            }),
            'avatar': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }
