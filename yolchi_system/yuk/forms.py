from django import forms
from django.contrib.auth.models import User

class imageForm(forms.Form):
    image = forms.ImageField(label="تغییر عکس پروفایل",required=False)
    