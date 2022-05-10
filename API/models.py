from lib2to3.pgen2.token import OP
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

OPTIONS = [
    ("WEB", "Website & Software"),
    ("UI", "UI/UX")
]

class UserProfile(AbstractUser):
    username = models.CharField(max_length=120, unique=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(('password'), max_length=128, help_text=("use'[algo]$[salt]$[hexdigest]'"))
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.username

class User_Profile_creation(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    profile = models.ImageField()
    description = models.TextField()
    contact = models.IntegerField()
    category = models.CharField(choices=OPTIONS, default="WEB",max_length=100)
    resume = models.FileField(null=True)

    def __str__(self) -> str:
        return self.user_profile.username