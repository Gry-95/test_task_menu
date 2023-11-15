from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_menu, name='menu'),
    path('<str:choice>', views.show_choice, name='choice'),
]
