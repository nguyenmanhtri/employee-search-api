import logging

from django.test import TestCase
from django.urls import reverse

logger = logging.getLogger(__name__)


class EmployeeViewSetTests(TestCase):

    def test_get_employees_success(self):
        results = []
        for i in range(10):
            response = self.client.get(reverse("employees-list"))
            data = response.json()
            results.append(data)

        self.assertIn("Rate limit exceeded", str(results))
