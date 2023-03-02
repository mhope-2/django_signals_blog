from django.test import TestCase
from rest_framework.test import APITestCase
from django_dynamic_fixture import G
from .models import Employee

# Create your tests here.
class TestAppEndpoints(APITestCase):

    def test_request_phone_verify_for_new_profile(self):
        """
        test EmployeeProfile object created
        on Employee object post save
        :return:
        """
        emp_obj = G(Employee, first_name="John", last_name="Doe", email="jdoe@jdoe.com")

        # reload Employee model values from the database
        emp_obj.profile.refresh_from_db()

        # access EmployeeProfile via related_name (reverse access)
        # and assert related Employee object attributes
        self.assertEqual(emp_obj.profile.employee.first_name, "John")
        self.assertEqual(emp_obj.profile.employee.last_name, "Doe")
        self.assertEqual(emp_obj.profile.employee.email, "jdoe@jdoe.com")




