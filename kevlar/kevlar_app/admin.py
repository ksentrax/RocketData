from django.contrib import admin

from .models import Employee, Position, Level


def remove_inf_of_wage(modeladmin, request, queryset):
    queryset.update(total_wage=None)


admin.site.add_action(remove_inf_of_wage, 'Remove total wage')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'patronymic', 'position',
                    'monthly_wage', 'total_wage')
    list_filter = ('positions', 'level')


admin.site.register(Employee, EmployeeAdmin)


class LevelAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Level, LevelAdmin)


class PositionAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Position, PositionAdmin)
