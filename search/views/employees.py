import django_filters

from rest_framework import viewsets

from search.serializers.employees import EmployeeSerializer
from search.models import Employees

employee_fields = Employees._meta.get_fields()
field_names = [f.name for f in employee_fields]


class EmployeeFilterSet(django_filters.FilterSet):
    class Meta:
        model = Employees
        fields = {f: ["exact", "in", "icontains"] for f in field_names}


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that fetches employee info
    """

    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    filterset_class = EmployeeFilterSet
