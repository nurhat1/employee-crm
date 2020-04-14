from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Otdel(models.Model):
    name = models.CharField('Название отдела', max_length=100)
    phone = models.CharField('Телефон отдела', max_length=100)
    

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.name



class Position(models.Model):
    name = models.CharField('Должность', max_length=100)
    zarplata = models.PositiveSmallIntegerField('Зарплата сотрудника', default = 0)
    otdel = models.ForeignKey(Otdel, on_delete = models.SET_NULL, null = True)
    

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name



class Employee(models.Model):
    first_name = models.CharField('Имя сотрудника', max_length=100)
    last_name = models.CharField('Фамилия сотрудника', max_length=100)
    position = models.ForeignKey(Position, on_delete = models.SET_NULL, null = True)
    hired_date = models.DateField(default = datetime.date.today)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.first_name