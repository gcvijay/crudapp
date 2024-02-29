from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

# def validate_mail(value):
#     print(value,'this validation function')
#     lst = value.split('@')
#     if "@gmail.com" in lst:
#         return value
#     else:
#         raise ValidationError("This field accepts mail id of google only")

def validate_mail(value):
    if not value.endswith("@gmail.com"):
        raise ValidationError("This field accepts mail id of Google only")

class Registration(models.Model):
    name   = models.CharField(max_length=100)
    sur_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10,unique=False)
    email  = models.EmailField(unique=False,validators=[validate_mail])
    age  = models.IntegerField()
    occupation = models.TextField(max_length=500)





