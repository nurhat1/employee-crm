# Generated by Django 3.0.2 on 2020-02-29 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Otdel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название отдела')),
                ('phone', models.CharField(max_length=100, verbose_name='Телефон отдела')),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя сотрудника')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия сотрудника')),
                ('zarplata', models.PositiveSmallIntegerField(default=0, verbose_name='Зарплата сотрудника')),
                ('otdel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='uchet.Otdel')),
                ('position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='uchet.Position')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
    ]
