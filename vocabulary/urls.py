from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60) (MainPage.as_view()), name='home'),
    path('eng_rus/', cache_page(60) (MainPageEngRus.as_view()), name='EngRusVariant'),
    path('registration/',RegisterUser.as_view(), name='registration')
]
