from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # list_display = (
    #     'days',
    #     'time'
    # )
    # fields = (
    #     'days',
    #     'time'
    # )
    # ordering = ('time',)
    pass