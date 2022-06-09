from django.forms import ModelForm
from django import forms
from .models import expense

class login_form(forms.Form):
    get_username = forms.CharField(label='Your name', max_length=10)
    get_pass = forms.CharField(label='Your Password', max_length=20)

class expense(ModelForm):
    class Meta:
        model = expense
        fields = ['shop_name', 'expense', 'sh_date','owner_id']
