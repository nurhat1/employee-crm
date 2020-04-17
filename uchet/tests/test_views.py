from django.test import TestCase, Client
from django.urls import reverse
from uchet.models import Otdel, Position, Employee



class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.department_url = reverse('department', args=['1'])
        self.employees_url = reverse('employees')
        self.createDepartment_url = reverse('create_department')
        self.updateDepartment_url = reverse('update_department', args=['1'])
        self.createPosition_url = reverse('create_position')
        self.addEmployee_url = reverse('add_employee')
        self.updateEmployee_url = reverse('update_employee', args=['1'])
        self.otdel1 = Otdel.objects.create(
            name = 'Otdel1',
            phone = 111
        )
        self.position1 = Position.objects.create(
            name = 'Position1',
            zarplata = 200.000,
            otdel = self.otdel1
        )
        self.employee1 = Employee.objects.create(
            first_name = 'Tolegen',
            last_name = 'Atenov',
            position = self.position1
        )


    def test_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'uchet/dashboard.html')


    def test_department_GET(self):
        response = self.client.get(self.department_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'uchet/department.html')


    def test_employees_GET(self):
        response = self.client.get(self.employees_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'uchet/employees.html')


    def test_createDepartment_POST(self):
        response = self.client.post(self.createDepartment_url, {
            'name': 'Otdel2',
            'phone': 222
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Otdel.objects.get(id=2).name, 'Otdel2')


    def test_createDepartment_POST_no_data(self):
        response = self.client.post(self.createDepartment_url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(Otdel.objects.count(), 1)

    
    def test_updateDepartment_POST(self):
        response = self.client.post(self.updateDepartment_url,{
            'name': 'Otdel1_updated',
            'phone': 111
        })
        self.otdel1.name = 'Otdel1_updated'

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.otdel1.name, 'Otdel1_updated')
        self.assertEquals(self.otdel1.phone, 111)


    def test_updateDepartment_POST_no_data(self):
        response = self.client.post(self.updateDepartment_url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(Otdel.objects.count(), 1)


    def test_createPosition_POST(self):
        response = self.client.post(self.createPosition_url, {
            'name': 'Position2',
            'zarplata': 100.000,
            'otdel': self.otdel1.id
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.otdel1.position_set.get(id=2).name, 'Position2')


    def test_createPosition_POST_no_data(self):
        response = self.client.post(self.createPosition_url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.otdel1.position_set.count(), 1)


    def test_addEmployee_POST(self):
        response = self.client.post(self.addEmployee_url, {
            'first_name': 'Azamat',
            'last_name': 'Batirov',
            'position': self.position1.id
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.position1.employee_set.get(id=2).first_name, 'Azamat')


    def test_addEmployee_POST_no_data(self):
        response = self.client.post(self.addEmployee_url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(Employee.objects.count(), 1)

    

    def test_updateEmployee_POST(self):
        employee2 = self.position1.employee_set.create(
            first_name = 'Azamat',
            last_name = 'Batirov',
            position = self.position1
        )

        response = self.client.post(self.updateEmployee_url, {
            'first_name': 'Azamat',
            'last_name': 'Zhigitov',
            'position': self.position1.id
        })

        employee2.last_name = 'Zhigitov'
        employee2.save()

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.position1.employee_set.get(id=2).last_name, 'Zhigitov')
        self.assertEquals(self.position1.employee_set.get(id=2).first_name, 'Azamat')
    
    
        

