from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('<int:zodiac>', views.get_zodiac_by_number),
    path('<str:zodiac>', views.get_zodiac, name='horoscope-name' ),
]