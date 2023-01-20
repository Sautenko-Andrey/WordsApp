from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class TypeEngWord(forms.ModelForm):
    '''Форма, которая будет принимать от пользователя
     назавание товара и сохранять его в БД
     для дальнейшей обработки.'''

    __USER_REQUEST_MAX_LENGTH = 50


    widgets = {
        'eng': forms.TextInput(attrs={'class': 'form-input'}),
    }

    class Meta:
        model = UserEngAnswer
        fields = ('eng_answer',)

    def clean_user_answer(self):
        eng_answer = self.cleaned_data['eng_answer']
        if self.__USER_REQUEST_MAX_LENGTH < len(eng_answer):
            raise ValidationError('Вы ввели слишком много букв...')
        return eng_answer


class RegisterUserForm(UserCreationForm):
    '''Собственная форма регистрации пользователя на сайте'''

    username=forms.CharField(label='Логин',widget=forms.TextInput(attrs={'class':'form-input'}))
    password1 = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class':'form-input'}))
    password2 = forms.CharField(label='Повтори пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    email=forms.CharField(label='email',widget=forms.EmailInput(attrs={'class':'form-input'}))

    class Meta:
        model=User
        fields=('username','password1','password2','email')