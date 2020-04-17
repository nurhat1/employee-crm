from django.test import SimpleTestCase, TestCase
from uchet.forms import OtdelForm, PositionForm, EmployeeForm
from uchet.models import Otdel, Position



class TestForms(TestCase):

    def setUp(self):
        self.otdel1 = Otdel.objects.create(
            name = 'Otdel',
            phone = 111
        )
        self.position1 = Position.objects.create(
            name = 'Position',
            zarplata = 150.000,
            otdel = self.otdel1
        )


    def test_otdel_form_valid_data(self):
        form = OtdelForm(data = {
            'name': 'Otdel1',
            'phone': 111
        })

        self.assertTrue(form.is_valid())


    def test_otdel_form_no_data(self):
        form = OtdelForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    
    def test_position_form_valid_data(self):
        form = PositionForm(data = {
            'name': 'Otdel1',
            'zarplata': 111,
            'otdel': self.otdel1.id
        })

        self.assertTrue(form.is_valid())


    def test_position_form_no_data(self):
        form = PositionForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)


    def test_employee_form_valid_data(self):
        form = EmployeeForm(data = {
            'first_name': 'Azamat',
            'last_name': 'Zhigitov',
            'position': self.position1.id
        })

        self.assertTrue(form.is_valid())


    def test_employee_form_no_data(self):
        form = EmployeeForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    

