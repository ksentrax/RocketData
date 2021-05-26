from django.db import models
from smart_selects.db_fields import ChainedForeignKey


class Level(models.Model):
    """Model representing a employee level."""
    title = models.CharField(max_length=50, verbose_name='Название')

    class Meta:
        verbose_name = 'Уровень'
        verbose_name_plural = 'Уровни'

    def __str__(self):
        return self.title


class Position(models.Model):
    """Model representing a employee position."""
    title = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.title


class Employee(models.Model):
    """Model representing a employee."""
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    patronymic = models.CharField(max_length=100,
                                  verbose_name='Отчество')
    employment_date = models.DateField(verbose_name='Дата приема')
    level = models.ForeignKey(Level,
                              on_delete=models.CASCADE,
                              verbose_name='Уровень')
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    monthly_wage = models.PositiveIntegerField(verbose_name='ЗП')
    total_wage = models.PositiveIntegerField(verbose_name='Выплачено',
                                             null=True,
                                             blank=True)
    authorities = ChainedForeignKey("self",
                                    chained_field="levels",
                                    chained_model_field="levels",
                                    show_all=False,
                                    auto_choose=True,
                                    null=True,
                                    blank=True)
    owner = models.ForeignKey('auth.User',
                              on_delete=models.CASCADE,
                              related_name='employees')

    class Meta:
        verbose_name = 'Данные сотрудника'
        verbose_name_plural = 'Данные сотрудников'

    def __str__(self):
        return self.last_name
