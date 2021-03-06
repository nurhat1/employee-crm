# Generated by Django 3.0.2 on 2020-02-29 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uchet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='otdel',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='zarplata',
        ),
        migrations.AddField(
            model_name='position',
            name='otdel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='uchet.Otdel'),
        ),
        migrations.AddField(
            model_name='position',
            name='zarplata',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Зарплата сотрудника'),
        ),
    ]
