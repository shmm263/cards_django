from django import forms
from .models import Patient,MedExamination


class RenewStatusForm(forms.Form):
    status_choices = (
        ('Да', 'Да'),
        ('Нет', 'Нет'),
    )
    renewal_status = forms.ChoiceField(label='Новий статус',choices=status_choices)
    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_status']
        # Помните, что всегда надо возвращать "очищенные" данные.
        return data

