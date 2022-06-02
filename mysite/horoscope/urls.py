from django.urls import path
from . import views
urlpatterns = [
    path('<zodiac>/', views.get_zodiac),
]