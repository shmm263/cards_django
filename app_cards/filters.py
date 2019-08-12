import django_filters
from .models import MedExamtList ,PatientList


class PosteFilterMedExamView(django_filters.FilterSet):
    patient_status = django_filters.CharFilter(lookup_expr='icontains')
    patient = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
       model = MedExamtList
       fields = {'patient_status', 'patient'}


class PosteFilterView(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    addr_city = django_filters.CharFilter(lookup_expr='icontains')
    phone_mobile = django_filters.CharFilter(field_name='phone_mobile', lookup_expr='icontains')
    inn = django_filters.CharFilter(field_name='inn', lookup_expr='icontains')
    class Meta:
       model = PatientList
       fields = {'patient', 'addr_city', 'phone_mobile','inn'}