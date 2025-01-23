from django import forms
from .models import Car

class imageForm(forms.Form):
    image = forms.ImageField(label="تغییر عکس پروفایل",required=False)

class carForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            'model',
            'year',
            'capacity',
            'type',
        ]
        labels = {
            'model': ' نام خودرو',
            'year': 'سال ساخت',
            'capacity': 'ظرفیت',
            'type': 'نوع باربر',
        }
        help_texts = {
            'capacity': 'کیلوگرم',
        }
        widgets = {
            'model': forms.TextInput(attrs={'placeholder': 'مثال: پیکان وانت'}),
        }
    