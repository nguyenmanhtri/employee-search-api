import logging

from django.test import TestCase
from django.urls import reverse

from search.models.models import Employees

logger = logging.getLogger(__name__)


class EmployeeViewSetTests(TestCase):
    def setUp(self):
        Employees.objects.create(
            first_name="tri",
            last_name="nguyen",
            email="tri@mail.com",
            telephone="+84123123123",
            department="tech",
            position="developer",
            location="ho chi minh city",
            status="Active",
            company="lorem ipsum",
        )
        Employees.objects.create(
            first_name="john",
            last_name="doe",
            email="john.doe@mail.com",
            telephone="+85123123123",
            department="tech",
            position="developer",
            location="ho chi minh city",
            status="Terminated",
            company="lorem ipsum",
        )

    def test_get_employees_success(self):
        response = self.client.get(reverse("employees-list"))
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["count"], 2)

    def test_get_employees_query_dynamic_fields(self):
        query_params = {
            "status": "Active",
            "fields": "department,location,position",
        }
        response = self.client.get(reverse("employees-list"), data=query_params)
        data = response.json()
        first_item = data["results"][0]

        self.assertEqual(response.status_code, 200)
        self.assertIn("department", first_item)
        self.assertIn("location", first_item)
        self.assertIn("position", first_item)
        self.assertNotIn("first_name", first_item)
