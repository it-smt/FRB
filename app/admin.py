from django.contrib import admin
from app.models import Trainer, Schedule, Event


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    """Модель тренера в админке."""
    list_display = (  # данные, которые будут отображаться в админке.
        'surname',
        'name',
        'patronymic',
        'experience',
    )
    fields = (  # Поля для заполнения, которые будут отображаться в админке.
        ('surname', 'name', 'patronymic'),
        'education',
        'experience',
        'description',
        'image'
    )
    search_fields = ('surname',)  # Поиск по фамилии
    ordering = ('experience',)  # Сортируется по опыту (от более опытного до неопытного).


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    """Модель расписания в админке."""
    list_display = (  # данные, которые будут отображаться в админке.
        'days',
        'time'
    )
    fields = (  # Поля для заполнения, которые будут отображаться в админке.
        'days',
        'time'
    )
    ordering = ('time',)  # Сортировка по времени.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Модель мероприятия в админке."""
    list_display = (
        'title',
        'event_place',
        'date'
    )
    fields = (
        'image',
        'title',
        ('event_place', 'date'),
        'description'
    )
    ordering = ('date',)
