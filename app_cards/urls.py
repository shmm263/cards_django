from django.conf.urls import include, url
from django.conf import settings
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^patients/$', views.PatientListView.as_view(), name='patients'),
    url(r'^Patient/(?P<pk>\d+)$', views.PatientDetailView.as_view(), name='patient-detail'),
    #url(r'^medexamination/(?P<pk>\d+)$', views.MedExaminationDetailView.as_view(), name='medexamination-detail'),
    url(r'^medexamination/(?P<pk>[-\w]+)/renew/$', views.medexamination_update_status, name='renew-status-medexamination'),
 #   url(r'^people/$', views.FilteredPersonListView.as_view(), name='people'),
    url(r'^patient/$', views.PatientListView.as_view(), name='patient'),
    url(r'^people1/$', views.MedExamListView.as_view(), name='people1'),
]