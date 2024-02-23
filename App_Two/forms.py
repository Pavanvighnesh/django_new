from django import forms
from App_Two.models import user

class myform(forms.ModelForm):
    class Meta():
        model=user
        fields='__all__'