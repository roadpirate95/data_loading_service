from django import forms

from app.models import Employee


class DateInput(forms.DateInput):
    input_type = 'date'


class PersonForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'date_of_birth': DateInput(),
        }
