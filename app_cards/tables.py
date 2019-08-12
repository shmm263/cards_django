import datetime
import django_tables2 as tables
from django_tables2 import A

from .models import Patient, MedExamtList, PatientList

class MedExaminationsTable(tables.Table):
    patient = tables.LinkColumn('patient-detail', args=[A('patient_id')])
    patient_status = tables.LinkColumn('renew-status-medexamination', args=[A('mid')])
    #purpose_medical_examination=tables.Column()
    class Meta:
            model = MedExamtList
            template_name = 'django_tables2/bootstrap.html'
            fields = ('patient', 'patient_status', 'purpose_medical_examination', 'date_medical_examination', 'dat_end', 'date_update')
            attrs = {"class": "table-striped table-bordered "}

class PatientTables(tables.Table):
    patient = tables.LinkColumn('patient-detail', args=[A('pid')])
    class Meta:
        model = PatientList
        template_name = 'django_tables2/bootstrap.html'
        # add class="paleblue" to <table> tag
        #attrs = {'class': 'paleblue'}
        #fields = ('first_name', 'addr_city', 'phone_mobile')
        attrs = {"class": "table-striped table-bordered "}





