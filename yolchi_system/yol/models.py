from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from yuk.models import Advertisement

def phone_start_with_0(value):
    if value[0] != '0' and value[1] != 9:
        raise ValidationError('Phone number must be started with 09')

class Driver(models.Model):
    profilePicture = models.ImageField(upload_to='yol_pictures/', default='yol_pictures/profile.png')
    phone = models.CharField(max_length=11,validators=[phone_start_with_0])
    licenseCode = models.CharField(max_length=10)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
class Car(models.Model):
    model = models.CharField(max_length=200,blank=True)

    TYPE = (
        ('V','وانت بار'),
        ('N','وانت نیسان'),
        ('K','کامیونت'),
        ('T','تریلی'),
    )
    type = models.CharField(max_length=1,choices=TYPE,blank=True)
    year = models.IntegerField(default=0)
    capacity = models.IntegerField(default=0)
    licensePlate = models.CharField(max_length=9,blank=True,null=True)
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.driver.user} : {self.model}"
    
class Waybill(models.Model):
    pickup_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(auto_now_add=True)

    STATUS = (
        ('W','پذیرفته شده توسط راننده'),
        ('S','در حال بارگیری'),
        ('T','در حال حمل'),
        ('R','گزارش'),
        ('A','تحویل بار'),
        ('N','ناتمام')
    )
    status = models.CharField(max_length=1,choices=STATUS,default='W')
    advertisement = models.OneToOneField(Advertisement, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return f"{self.advertisement.title}"

class Report(models.Model):
    date = models.DateTimeField(auto_now_add=True)

    TYPE = (
        ('A','تصادف'),
        ('R','سرقت از محموله'),
        ('B','خرابی خودروی باربری'),
        ('W','آب و هوای نامساعد'),
    )
    type = models.CharField(max_length=1,choices=TYPE)
    description = models.TextField()

    STATUS = (
        ('W','در حال پیگیری گزارش'),
        ('S','رفع گزارش و ادامه مسیر'),
        ('N','عدم توانایی در ادامه حمل بار'),
    )
    status = models.CharField(max_length=1,choices=STATUS,default="W")
    Waybill = models.ForeignKey(Waybill, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Waybill.advertisement.title} : {self.type}"


