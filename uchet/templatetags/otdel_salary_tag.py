from django import template
from uchet.models import Otdel, Position

register = template.Library()


# чтобы тег заработал, надо перезапустить сервер
@register.simple_tag()
def get_otdel_salary(dep_name):
    '''Вывод общего фонда отдела'''
    department = Otdel.objects.get(name = dep_name)
    otdel_salary_fund = 0
    for position in department.position_set.all():
        otdel_salary_fund += (position.zarplata * position.employee_set.count())
    return otdel_salary_fund


@register.simple_tag()
def get_otdel_employees(dep_name):
    '''Вывод всех работников отдела'''
    department = Otdel.objects.get(name = dep_name)
    otdel_employees = []
    for position in department.position_set.all():
        for employee in position.employee_set.all():
            otdel_employees.append(employee)

    return otdel_employees


@register.simple_tag()
def get_total_salary():
    departments = Otdel.objects.all()
    total_salary = 0
    for dep in departments:
        total_salary += get_otdel_salary(dep.name)

    return total_salary