from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(User)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
    )


class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'address',
    )


class MenuAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'restaurant',
        'menu',
        'votes',
    )


class VoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'menu')


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Vote, VoteAdmin)