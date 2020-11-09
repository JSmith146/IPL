import django_filters
from django_filters import DateFilter

from .models import *

class ProjectFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name = 'project_start_date', lookup_expr='gte', label="Start Date")
    end_date = DateFilter(field_name = 'project_due_date', lookup_expr='lte', label="End Date")
    class Meta:
        model = Project
        fields = ['project_status']
