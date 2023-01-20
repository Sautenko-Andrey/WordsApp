from django import template
from vocabulary.models import *
from random import randint

#оздадим экземпляр класса Library,
# через который происходит регистрация собственных шаблонных тегов
register=template.Library()

class WordFromData:
    def __init__(self):
        self.WORD_PK=randint(1,4)
    @register.simple_tag()
    def show_rus_word(self):
        '''Тэг, который берет случайное слово на русском из БД'''


        return AllWords.objects.get(pk=self.WORD_PK).rus

    @register.simple_tag()
    def show_eng_word(self):
        return AllWords.objects.get(pk=self.WORD_PK).eng


@register.simple_tag()
def get_user_eng_answer():
    '''Тэг, который берет ответ пользователя на английском из БД'''
    return UserEngAnswer.objects.latest('time_create').eng_answer