import datetime

from django.db import models


class Trainer(models.Model):
    """Модель тренера."""
    surname = models.CharField(verbose_name='Surname', max_length=50)
    name = models.CharField(verbose_name='Name', max_length=50)
    patronymic = models.CharField(verbose_name='Patronymic', max_length=50, blank=True)
    education = models.TextField(verbose_name='Education')
    experience = models.PositiveSmallIntegerField(verbose_name='Experience', default=0)
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(verbose_name='Image', upload_to='trainers_images', null=True, blank=True,
                              default='/trainers_images/default-avatar.png')


class Schedule(models.Model):
    """Модель расписания."""
    days = models.CharField(verbose_name='Days', max_length=100)
    time = models.TextField(verbose_name='Time',
                            max_length=1000)  # Представляет собой текстовой поле, где можно написать время занятий и добавить заметки к ним.

    def get_list(self):
        """Возвращает список расписания."""
        return self.time.split('\r\n')


class Event(models.Model):
    """Модель мероприятия."""
    image = models.ImageField(verbose_name='Image', upload_to='events_images', null=True, blank=True)
    title = models.CharField(verbose_name='Title', max_length=200)
    event_place = models.CharField(verbose_name='Event Place', max_length=255)
    description = models.TextField(verbose_name='Description', max_length=10000)
    date = models.DateTimeField(verbose_name='Date And Time', default=datetime.datetime.utcnow())

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
