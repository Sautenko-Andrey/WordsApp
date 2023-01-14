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

    def check_user_answer(self):
        user_answer=get_user_eng_answer


    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)

        context_dict['rus_word'] = get_rus_word
        user_eng_answer=get_user_eng_answer
        if user_eng_answer==get_rus_word.eng:
            context_dict['result']='правильно!'
        else:
            context_dict['result']='неправильно!'

        mutual_context_dict = self.get_user_context(title='Проверь свой словарный запас')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')