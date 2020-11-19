from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Create your models here.
class UserProfile(models.Model):
    gender_choices = {
        ("male", "Male"),
        ("female", "Female"),
    }
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    pincode_regex = RegexValidator(
        regex=r'\d{6}',
        message="Pincode must be of six digits."
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=6, choices=gender_choices)
    contact = models.CharField(max_length=17, validators=[phone_regex], blank=True)
    address = models.CharField(max_length=200, blank=True)
    pincode = models.IntegerField(validators=[pincode_regex], blank=True)
