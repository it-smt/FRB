from django import forms
from app.models import Trainer, Schedule


class TrainerForm(forms.ModelForm):
    """Форма тренера."""
    surname = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={
        'class': 'form__input',
        'placeholder': 'Фамилия'
    }))
    name = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={
        'class': 'form__input',
        'placeholder': 'Имя'
    }))
    patronymic = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={
        'class': 'form__input',
        'placeholder': 'Отчество(если есть)'
    }), required=False)
    education = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'form__input form__textarea',
        'placeholder': 'Образование'
    }))
    experience = forms.IntegerField(label='', widget=forms.NumberInput(attrs={
        'class': 'form__input',
        'placeholder': 'Опыт'
    }))
    description = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'form__input form__textarea',
        'placeholder': 'Описание'
    }))
    image = forms.ImageField(label='', widget=forms.FileInput(attrs={'class': 'form__image'}),
                             required=False)

    class Meta:
        model = Trainer
        fields = (
            'surname',
            'name',
            'patronymic',
            'education',
            'experience',
            'description',
            'image'
        )


class ScheduleForm(forms.ModelForm):
    """Форма расписания."""
    days = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form__input',
        'placeholder': 'Дни недели (Пн, Ср, Пт)'
    }))
    time = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'form__input',
        'placeholder': 'Время + заметки (11:20 - Сборники GreenPark)'
    }))

    class Meta:
        model = Schedule
        fields = (
            'days',
            'time'
        )
