from django.urls import path
from app import views as app_views

app_name = 'news'

urlpatterns = [
    path('', app_views.in_development, name='index'),  # Новости.
]