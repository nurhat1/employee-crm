from django.contrib import admin
from .models import Otdel, Position, Employee

# Register your models here.
admin.site.register(Otdel)
admin.site.register(Position)
admin.site.register(Employee)