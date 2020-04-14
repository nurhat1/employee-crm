from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .models import Otdel, Position, Employee
from django.db.models import Sum


from .forms import OtdelForm, EmployeeForm, PositionForm

# Create your views here.


#------------HOME----------------------
def home(request):
    departments = Otdel.objects.all()

    #GET request
    if request.method == 'GET':
        dep_name = request.GET.get('search_name')
        dep_phone = request.GET.get('search_phone')
        if dep_name:
            departments = Otdel.objects.filter(name__contains = dep_name)
        if dep_phone:
            departments = Otdel.objects.filter(phone__contains = dep_phone)

    context = {
        'departments': departments
    }
    return render(request, 'uchet/dashboard.html', context)




#------------DEPARTMENT----------------------
def department(request, pk_dep):
    department = Otdel.objects.get(id = pk_dep)
    positions = Position.objects.filter(otdel__name = department.name)
    pos_count = Position.objects.filter(otdel__name=department.name).count()
    emp_count = Employee.objects.filter(position__otdel__name=department.name).count()

    #сумма зарплат должностей
    salary_fund = Position.objects.filter(otdel__name=department.name).aggregate(Sum('zarplata'))

    salary_fund_main = 0


    #Count salary fund of department
    for position in positions:
        salary_fund_main += position.employee_set.all().count() * position.zarplata


    #if salary_fund == None
    salary_fund = salary_fund['zarplata__sum']
    if salary_fund is None:
        salary_fund = 0


    context = {
        'department': department,
        'positions': positions,
        'pos_count': pos_count,
        'emp_count': emp_count,
        'salary_fund': salary_fund,
        'salary_fund_main': salary_fund_main,
    }

    return render(request, 'uchet/department.html', context)



#------------EMPLOYEES----------------------
def employees(request):
    employees = Employee.objects.all()
    departments = Otdel.objects.all()
    positions = Position.objects.all()

    #GET request
    if request.method == 'GET':
        emp_name = request.GET.get('search_name')
        dep_name = request.GET.get('select_dep')
        pos_name = request.GET.get('select_pos')
        if emp_name:
            employees = Employee.objects.filter(last_name__icontains = emp_name)
        if dep_name:
            employees = Employee.objects.filter(position__otdel__name=dep_name)
        if pos_name:
            employees = Employee.objects.filter(position__name=pos_name)

    context = {
        'employees': employees,
        'departments': departments,
        'positions': positions
    }
    return render(request, 'uchet/employees.html', context)




#------------CREATE DEPARTMENT----------------------
def createDepartment(request):
    form = OtdelForm()


    #POST request
    if request.method == 'POST':
        form = OtdelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'uchet/department_form.html', context)




#------------UPDATE DEPARTMENT----------------------
def updateDepartment(request, pk_dep):

    department = Otdel.objects.get(id = pk_dep)

    #update department form  
    form = OtdelForm(instance=department)

    #POST request
    if request.method == 'POST':
        form = OtdelForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'uchet/department_form.html', context)



#------------CREATE POSITION----------------------
def createPosition(request):
    form = PositionForm()

    #POST request
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'uchet/position_form.html', context)




#------------ADD EMPLOYEE----------------------
def addEmployee(request):
    form = EmployeeForm()

    #POST request
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees')

    context = {
        'form': form
    }
    return render(request, 'uchet/employee_form.html', context)




#------------UPDATE EMPLOYEE----------------------
def updateEmployee(request, pk_emp):
    employee = Employee.objects.get(id = pk_emp)

    #update employee form
    form = EmployeeForm(instance = employee)

    #POST request
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees')

    context = {
        'form': form
    }
    return render(request, 'uchet/employee_form.html', context)




#------------DELETE EMPLOYEE----------------------
def deleteEmployee(request, pk_emp):
    Employee.objects.get(id = pk_emp).delete()
    return redirect('employees')




#------------REPLACE EMPLOYEES----------------------
def replaceEmployees(request, pk_dep):
    departments = Otdel.objects.all()
    from_dep = Otdel.objects.get(id = pk_dep)

    #POST request
    if request.method == 'POST':
        #найти выбранный отдел для перенесения
        dep_name = request.POST.get('select_dep')
        to_dep = Otdel.objects.get(name = dep_name)

        #найти все должности отдела, которую нужно перенести
        replaced_positions = Position.objects.filter(otdel__name = from_dep.name)
        for position in replaced_positions:
            #изменить отдел каждой должности на выбранную
            position.otdel = to_dep
            position.save()

        return redirect('/')

    context = {
        'departments': departments,
        'department': from_dep
    }

    return render(request, 'uchet/replace_employees.html', context)




#------------GET REPORT----------------------
def getReport(request):
    #список сотрудников по отделам
    #фонд зарплаты каждого отдела
    #общий фонд

    departments = Otdel.objects.all()
    employees = Employee.objects.all()


    context = {
        'departments': departments,
        'employees': employees
    }


    return render(request, 'uchet/report.html', context)

 