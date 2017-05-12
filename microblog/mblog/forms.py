from django import forms

from .models import MBlog

class UpdateMBForm(forms.ModelForm) : 
    class Meta : 
        model = MBlog
        fields = ['content']