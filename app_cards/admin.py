from django.contrib import admin

# Register your models here.
from .models import  LookupRegion, LookupRajon,Patient, MedExamination

#admin.site.register(Genre)
# admin.site.register(Region)
# admin.site.register(Rajon)
# admin.site.register(patient)

# Register the Admin classes for Bosok using the decorator

@admin.register(LookupRegion)
class LookupRegionAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for BookInstance using the decorator

@admin.register(LookupRajon)
class LookupRajonAdmin(admin.ModelAdmin):
    list_display = ('rajons', 'region')
    list_filter = ['region']
    search_fields = ['rajons']


class PatientAdmin(admin.ModelAdmin):
  # form = MyPatientForm
   list_display = ('first_name', 'last_name', 'date_birthday','region','inn','email')
   exclude = ['date_update']
   list_filter = ['last_name', 'first_name','region']
   search_fields = ['first_name','inn', 'email']
   autocomplete_fields = ['rajon']
   # Register the admin class with the associated model

admin.site.register(Patient, PatientAdmin)


@admin.register(MedExamination)
class MedExaminationAdmin(admin.ModelAdmin):
    list_display = ('patient', 'date_medical_examination','purpose_medical_examination','dat_end')
    exclude = ['date_update']
    list_filter = ['date_medical_examination']
    search_fields = ['patient__first_name', 'patient__email', 'patient__inn']
    autocomplete_fields = ['patient']