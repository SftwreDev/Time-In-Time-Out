from django import forms

from .models import TimeInTimeOut


class TimeInTimeOutForms(forms.ModelForm):
    class Meta:
        model = TimeInTimeOut
        fields = "__all__"