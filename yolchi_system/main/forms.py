from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        labels = {
            'username': 'نام کاربری',
            'password': 'رمزعبور',
        }
        widgets = {
            'password': forms.PasswordInput(),
        }
        help_texts = {
            'username': '',
        }

class UserRegistrationForm(forms.ModelForm):
    OPTIONS = [
        ('driver', 'راننده'),
        ('shipper', 'صاحب بار'),
    ]

    userType = forms.ChoiceField(
        choices=OPTIONS,
        widget=forms.RadioSelect,
        label='ثبت نام به عنوان :',
    )
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]
        labels = {
            'username': 'نام کاربری',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'email': 'پست الکترونیکی',
            'password': 'رمزعبور',
        }
        widgets = {
            'password': forms.PasswordInput(),
        }
        help_texts = {
            'username': ' 150 کاراکتر یا کمتر. فقط حروف، ارقام و @/./+/-/_.',
        }
