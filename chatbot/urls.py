from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path("submit/",views.speech_to_text,name='speech_to_text')
]