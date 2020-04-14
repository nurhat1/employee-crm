from django.forms import ModelForm
from .models import Otdel, Employee, Position

class OtdelForm(ModelForm):
    class Meta:
        model = Otdel
        fields = '__all__'


class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = '__all__'



class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['hired_date']