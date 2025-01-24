from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

def phone_start_with_0(value):
    if value[0] != '0' and value[1] != 9:
        raise ValidationError('Phone number must be started with 09')

class Shipper(models.Model):
    profilePicture = models.ImageField(upload_to='yuk_pictures/', default='yuk_pictures/profile.png')
    phone = models.CharField(max_length=11,validators=[phone_start_with_0])
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
      
class Advertisement(models.Model):
    title = models.CharField(max_length=200)
    shipper = models.ForeignKey(Shipper, on_delete=models.CASCADE)
    description = models.TextField()
    freight = models.IntegerField(null=True)

    STATUS = (
        ('P','در حال انتظار'),
        ('A','پذیرفته شده'),
    )
    status = models.CharField(max_length=1,choices=STATUS,default='P')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-date"]
    

class Cargo(models.Model):
    weight = models.FloatField()
    type = models.CharField(max_length=200)
    value = models.FloatField()
    dimension = models.CharField(max_length=200)
    special_instructions = models.TextField(blank=True)
    advertisement = models.OneToOneField(Advertisement, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.advertisement.title} : {self.weight} کیلوگرم"


class Route(models.Model):
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    dest_city =  models.CharField(max_length=200,blank=True,null=True)
    origin_city =  models.CharField(max_length=200,blank=True,null=True)
    distance = models.CharField(max_length=200)
    estimated_time = models.CharField(max_length=200)
    advertisement = models.OneToOneField(Advertisement, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.advertisement.title} : {self.origin_city} به {self.dest_city}"
