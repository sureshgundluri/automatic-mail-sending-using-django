from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    profile_user=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.TextField()
    Profile_pic=models.ImageField(upload_to='suresh')
