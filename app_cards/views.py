from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
#from requests import request

from .models import PatientList, Patient, MedExamtList, MedExamination
from django.views import generic
import datetime
# Create your views here.
from .tables import  PatientTables, MedExaminationsTable
from .filters import PosteFilterView, PosteFilterMedExamView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .forms import RenewStatusForm
from django.shortcuts import get_object_or_404


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_patients = Patient.objects.all().count()
    # num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    # num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    # num_authors = Author.objects.count()  # Метод 'all()' применен по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_patients': num_patients, },
    )

# Create your views here.

class PatientDetailView(generic.DetailView):
 model = Patient
 template_name = 'app_cards/patient_details.html'


class PatientListView(SingleTableMixin, FilterView):
    table_class = PatientTables
    model = PatientList
    template_name = 'app_cards/patient.html'
    filterset_class = PosteFilterView
    table_pagination = {
        'per_page': 25
    }

class MedExamListView(SingleTableMixin, FilterView):
    table_class = MedExaminationsTable
    model = MedExamtList
    template_name = 'app_cards/people1.html'
    filterset_class = PosteFilterMedExamView
    table_pagination = {
        'per_page': 25
    }

def medexamination_update_status(request, pk):
    mde_inst = get_object_or_404(MedExamination, pk=pk)
    if request.method == 'POST':
        form = RenewStatusForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            #book_inst.due_back = form.cleaned_data['renewal_date']
            mde_inst.patient_status = form.cleaned_data['renewal_status']
            #mde_inst.date_update= datetime.date.today()
            mde_inst.save()
            return HttpResponseRedirect(reverse('people1'))
    else:
         proposed_renewal_status = mde_inst.patient_status
    #    form = RenewBookForm(initial={'renewal_date': proposed_renewal_status,})
         form = RenewStatusForm(initial={'renewal_status': proposed_renewal_status, })

    return render(request, 'app_cards/MedExamination_detail.html', {'form': form, 'mde_inst': mde_inst})