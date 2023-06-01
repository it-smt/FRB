from django.shortcuts import render, HttpResponseRedirect, reverse
from app.models import Trainer, Schedule, Event
from app.forms import TrainerForm, ScheduleForm


def index(request):
    """Функция обработчик главной страницы."""
    context = {
        'title': 'ФРБНВ'
    }
    return render(request, 'app/index.html', context)


def trainers(request):
    """Функция обработчик страницы тренеров."""
    context = {
        'title': 'ФРБНВ | Тренера',
        'trainers': Trainer.objects.all(),
    }
    return render(request, 'app/trainers.html', context)


def trainer_detail(request, pk):
    """Функция обработчик страницы тренера."""
    trainer = Trainer.objects.get(id=pk)
    context = {
        'title': f'ФРБНВ | {trainer.surname} {trainer.name[:1]}. {trainer.patronymic[:1]}.',
        'trainer': trainer
    }
    return render(request, 'app/trainer_detail.html', context)


def add_trainer(request):
    """Функция обработчик формы добавления тренера."""
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app:trainers'))
    else:
        form = TrainerForm()
    context = {
        'title': 'ФРБНВ | Добавление тренера',
        'form': form,
    }
    return render(request, 'app/add_trainer.html', context)


def delete_trainer(request, pk):
    """Функция обработчик удаления тренера."""
    trainer = Trainer.objects.get(id=pk)
    trainer.delete()
    return HttpResponseRedirect(reverse('app:trainers'))


def edit_trainer(request, id):
    """Функция обработчик формы изменения тренера."""
    trainer = Trainer.objects.get(id=id)
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            trainer.surname = request.POST.get('surname')
            trainer.name = request.POST.get('name')
            trainer.patronymic = request.POST.get('patronymic')
            trainer.education = request.POST.get('education')
            trainer.experience = request.POST.get('experience')
            trainer.description = request.POST.get('description')
            trainer.image = request.FILES.get('image')
            print(request.FILES)
            trainer.save()
            return HttpResponseRedirect(reverse('app:trainers'))
    else:
        form = TrainerForm(data={
            'surname': trainer.surname,
            'name': trainer.name,
            'patronymic': trainer.patronymic,
            'education': trainer.education,
            'experience': trainer.experience,
            'description': trainer.description,
        }, files={'image': trainer.image})
    context = {
        'title': 'ФРБНВ | Редактирование тренера',
        'trainer': trainer,
        'form': form
    }
    return render(request, 'app/trainer_edit.html', context)


def show_schedules(request):
    """Функция обработчик страницы с расписанием."""
    schedules = Schedule.objects.all()
    context = {
        'title': 'ФРБНВ | Расписание',
        'schedules': schedules,
    }
    return render(request, 'app/schedules.html', context)


def add_schedule(request):
    """Функция обработчик формы добавления расписания."""
    if request.method == 'POST':
        form = ScheduleForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app:show_schedules'))
    else:
        form = ScheduleForm()
    context = {
        'title': 'ФРБНВ | Добавление расписания',
        'form': form
    }
    return render(request, 'app/create_schedule.html', context)


def edit_schedule(request, pk):
    """Функция обработчик формы изменения расписания."""
    schedule = Schedule.objects.get(id=pk)
    if request.method == 'POST':
        form = ScheduleForm(data=request.POST)
        if form.is_valid():
            schedule.days = request.POST.get('days')
            schedule.time = request.POST.get('time')
            schedule.save()
            return HttpResponseRedirect(reverse('app:show_schedules'))
    else:
        form = ScheduleForm({'days': schedule.days, 'time': schedule.time})
    context = {
        'title': 'ФРБНВ | Редактирование расписания',
        'schedule': schedule,
        'form': form
    }
    return render(request, 'app/schedule_edit.html', context)


def delete_schedule(request, pk):
    """Функция обработчик удаления расписания."""
    schedule = Schedule.objects.get(id=pk)
    schedule.delete()
    return HttpResponseRedirect(reverse('app:show_schedules'))


def development_and_design(request):
    """Функция обработчик страницы разработчиков и дизайнеров."""
    context = {
        'title': 'ФРБНВ | Разработка и дизайн'
    }
    return render(request, 'app/development_and_design.html', context)


def events(request):
    """Функция обработчик страницы мероприятий."""
    context = {
        'title': 'ФРБНВ | Мероприятия',
        'events': Event.objects.all()
    }
    return render(request, 'app/events.html', context)


def contacts(request):
    """Функция обработчик страницы контактов."""
    context = {
        'title': 'ФРБНВ | Контакты',
    }
    return render(request, 'in_development.html', context)


def about(request):
    """Функция обработчик страницы о нас."""
    context = {
        'title': 'ФРБНВ | О нас',
    }
    return render(request, 'in_development.html', context)


def sign_up(request):
    pass


def in_development(request):
    context = {
        'title': 'ФРБНВ | В разработке'
    }
    return render(request, 'in_development.html', context)
