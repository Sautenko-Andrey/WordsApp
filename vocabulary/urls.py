from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('',  MainPage.as_view(), name='home'),
    path('eng_rus/', MainPageEngRus.as_view(), name='EngRusVariant'),
    path('registration/',RegisterUser.as_view(), name='registration'),
    path('login/', LoginUser.as_view(),name='login'),
    path('logout/', logout_user, name='logout')
]
