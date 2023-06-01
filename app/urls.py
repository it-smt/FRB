from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),  # Главная.
    path('trainers', views.trainers, name='trainers'),  # Тренера.
    path('trainers/<int:pk>', views.trainer_detail, name='trainer_detail'),  # Карточка тренера.
    path('trainers/add_trainer', views.add_trainer, name='add_trainer'),  # Форма добавления тренера.
    path('trainers/delete_trainer/<int:pk>', views.delete_trainer, name='delete_trainer'),  # Удаление тренера.
    path('trainers/edit_trainer/<int:id>', views.edit_trainer, name='edit_trainer'),  # Форма редактирования тренера.
    path('schedules', views.show_schedules, name='show_schedules'),  # Расписание.
    path('schedules/add_schedule', views.add_schedule, name='add_schedule'),  # Форма добавления расписания.
    path('schedules/edit_schedule/<int:pk>', views.edit_schedule, name='edit_schedule'),  # Форма редактирования расписания.
    path('schedules/delete_schedule/<int:pk>', views.delete_schedule, name='delete_schedule'),  # Удаление расписания.
    path('development_and_design', views.development_and_design, name='development_and_design'),  # Разработка и дизайн.
    path('events', views.events, name='events'),  # Мероприятия.
    path('contacts', views.in_development, name='contacts'),  # Контакты.
    path('about', views.in_development, name='about'),  # О нас.
    path('sign_up', views.in_development, name='sign_up'),  # Записаться.
    path('achievements', views.in_development, name='achievements'),  # Достижения.
]
