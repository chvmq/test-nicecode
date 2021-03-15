from django.urls import path
from .views import *
urlpatterns = [
    path('', index_form, name='index_form'),
    path('upload/', index_action_form, name='index_action_form'),
    path('detail/<str:slug>/', detail_photo, name='detail_photo'),
]
