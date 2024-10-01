from django_filters import FilterSet, NumberFilter, CharFilter

from main.models import StudyPlan

class StudyPlanFilter(FilterSet):
    groups = CharFilter(field_name='groups', lookup_expr='icontains')
    edu_year = NumberFilter(field_name='edu_year_id', lookup_expr='exact')
    edu_type = CharFilter(field_name='edu_type', lookup_expr='exact')
    confirm = NumberFilter(field_name='confirm', lookup_expr='exact')
    semester = CharFilter(field_name='semester', lookup_expr='exact')
    teacher_id = NumberFilter(field_name='teacher_id', lookup_expr='exact')
    class Meta:
        model = StudyPlan
        fields = ['groups', 'edu_year', 'edu_type', 'semester', 'confirm', 'teacher_id']