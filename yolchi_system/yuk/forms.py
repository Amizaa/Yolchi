from django import forms
from .models import Advertisement,Cargo

class imageForm(forms.Form):
    image = forms.ImageField(label="تغییر عکس پروفایل",required=False)
    
class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = [
            'weight',
            'type',
            'value',
            'dimension',
            'special_instructions',
        ]
        labels = {
            'weight': 'وزن بار',
            'type': 'نوع بار',
            'value': 'ارزش تقریبی بار',
            'dimension': 'مختصات و اندازه بار',
            'special_instructions': 'دستور العمل های خاص',
        }
        help_texts = {
            'weight': 'کیلوگرم',
            'value': 'تومان',
        }
        widgets = {
            'type': forms.TextInput(attrs={'placeholder': 'مثال: میوه و تره بار'}),
            'dimension': forms.TextInput(attrs={'placeholder': 'مثال: 1*3 متر'}),
            'description': forms.Textarea(
                attrs={'placeholder': 'Enter description here'}),
        }

class AdForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = [
            'title',
            'description',
            'freight',
        ]
        labels = {
            'title': 'عنوان',
            'description': 'توضیحات',
            'freight': 'کرایه حمل'
        }
        help_texts = {
            'freight': 'تومان',
        }

