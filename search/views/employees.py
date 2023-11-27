import django_filters

from rest_framework import viewsets

from search.serializers.employees import EmployeeSerializer
from search.models import Employees


class EmployeeFilterSet(django_filters.FilterSet):
    id = django_filters.NumberFilter()

    class Meta:
        model = Employees
        exclude = []


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that fetches employee info
    """

    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    filterset_fields = "__all__"
