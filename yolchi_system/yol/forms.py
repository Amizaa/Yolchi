from django import forms
from .models import Car,Report

class imageForm(forms.Form):
    image = forms.ImageField(label="تغییر عکس پروفایل",required=False)


class carForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            'model',
            'licensePlate',
            'year',
            'capacity',
            'type',
        ]
        labels = {
            'model': ' نام خودرو',
            'licensePlate': 'پلاک خودرو',
            'year': 'سال ساخت',
            'capacity': 'ظرفیت',
            'type': 'نوع باربر',
        }
        help_texts = {
            'capacity': 'کیلوگرم',
        }
        widgets = {
            'model': forms.TextInput(attrs={'placeholder': 'مثال: پیکان وانت'}),
            'licensePlate': forms.TextInput(attrs={'placeholder': 'مثال: 22و861-17'}),
        }
class reportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = [
            'type',
            'description',
        ]
        labels = {
            'type': 'نوع گزارش',
            'description': 'توضیحات',
        }

class reportStutusForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = [
            'status',
        ]
        labels = {
            'status': 'تغییر وضعیت گزارش',
        }

    