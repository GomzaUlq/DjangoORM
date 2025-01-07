from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин:')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Введите пароль(минимум 8 символов):')
    repeat_password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Подтвердите пароль:')
    age = forms.IntegerField(min_value=18, max_value=100, label='Введите возраст:')
