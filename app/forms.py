from django import forms

from .models import TimeInTimeOut, Category


class TimeInTimeOutForms(forms.ModelForm):
    class Meta:
        model = TimeInTimeOut
        fields = "__all__"


class CategoryForms(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'