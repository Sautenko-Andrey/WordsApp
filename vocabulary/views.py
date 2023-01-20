from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import *
from django.views.generic import CreateView

from .models import AllWords
from .utils import MutualContext

from .templatages.vocabulary_tags import *


class MainPage(MutualContext,CreateView):
    '''Класс-обработчик главной страницы приложения.'''

    form_class = TypeEngWord
    template_name = 'vocabulary/index.html'
    success_url = reverse_lazy('home')


    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)

        words=WordFromData()
        context_dict['rus_word'] = words.show_rus_word
        context_dict['user_answer'] = get_user_eng_answer
        context_dict['eng_word'] = words.show_eng_word
        # if get_user_eng_answer != words.show_eng_word:
        #     context_dict['result'] = ' Неправильно!'
        # elif get_user_eng_answer == words.show_eng_word:
        #     context_dict['result'] = 'Правильно!'


        mutual_context_dict = self.get_user_context(title='Проверь свой словарный запас')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))


class MainPageEngRus(MutualContext,CreateView):
    '''Класс-обработчик главной страницы приложения.'''

    form_class = TypeEngWord
    template_name = 'vocabulary/index2.html'
    success_url = reverse_lazy('home')


    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)

        words=WordFromData()
        context_dict['rus_word'] = words.show_rus_word
        context_dict['user_answer'] = get_user_eng_answer
        context_dict['eng_word'] = words.show_eng_word
        # if get_user_eng_answer != words.show_eng_word:
        #     context_dict['result'] = ' Неправильно!'
        # elif get_user_eng_answer == words.show_eng_word:
        #     context_dict['result'] = 'Правильно!'


        mutual_context_dict = self.get_user_context(title='Проверь свой словарный запас')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))


class RegisterUser(MutualContext,CreateView):
    '''Класс-представление, отвечающее за регистрацию пользователя на сайте'''
    form_class = RegisterUserForm
    template_name = 'vocabulary/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        mutual_context_dict = self.get_user_context(title='Регистрация')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')



