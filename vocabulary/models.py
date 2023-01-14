from django.db import models

class AllWords(models.Model):
    rus=models.CharField(max_length=25,null=False)
    eng=models.CharField(max_length=25,null=False)

    class Meta:
        verbose_name = 'Все слова приложения'
        verbose_name_plural = 'Все слова приложения'

class UserEngAnswer(models.Model):
    eng_answer=models.CharField(max_length=25,null=True)
    time_create = models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        verbose_name = 'Ответ пользователя на английском'
        verbose_name_plural = 'Ответ пользователя на английском'

