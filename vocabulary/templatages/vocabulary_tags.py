from django import template
from vocabulary.models import *
from random import randint

#оздадим экземпляр класса Library,
# через который происходит регистрация собственных шаблонных тегов
register=template.Library()


@register.simple_tag()
def get_rus_word():
    '''Тэг, который берет случайное слово на русском из БД'''
    word_pk=randint(1,4)
    return AllWords.objects.get(pk=word_pk)

@register.simple_tag()
def get_user_eng_answer():
    '''Тэг, который берет ответ пользователя на английском из БД'''
    return UserEngAnswer.objects.latest('time_create')