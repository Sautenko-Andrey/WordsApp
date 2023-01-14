from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import AllWords, UserEngAnswer
from .views import MainPage


class AllWordsAdmin(admin.ModelAdmin):
    list_display = ('rus', 'eng')
    list_display_links = ('rus','eng')

class UserEngAnswerAdmin(admin.ModelAdmin):
    list_display = ('eng_answer',)
    list_display_links = ('eng_answer',)

admin.site.register(AllWords, AllWordsAdmin)
admin.site.register(UserEngAnswer, UserEngAnswerAdmin)
