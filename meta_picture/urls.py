from django.urls import path
from .views import index_form, index_action_form
urlpatterns = [
    path('', index_form, name='index_form'),
    path('upload/', index_action_form, name='index_action_form'),
]
