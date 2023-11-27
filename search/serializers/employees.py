from search.models import Employees
from search.serializers.serializers import DynamicFieldsModelSerializer


class EmployeeSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Employees
        fields = "__all__"
