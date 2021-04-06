from django import forms

from .models import TimeInTimeOut, Category

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.DateInput):
    input_type = 'time'

class TimeInTimeOutForms(forms.ModelForm):
    class Meta:
        model = TimeInTimeOut
        fields = ['category','shift_date', 'time_in' , 'time_out',  'break_out','break_in', 'task']
        widgets = {
            'shift_date' : DateInput(),
            'time_in' : TimeInput(),
            'time_out' : TimeInput(),
            'break_in' : TimeInput(),
            'break_out' : TimeInput(),
        }

class CategoryForms(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'