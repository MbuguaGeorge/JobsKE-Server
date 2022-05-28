from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

OPTIONS = [
    ("Website & Software", "Website & Software"),
    ("UI/UX", "UI/UX")
]

JOBTYPE = [
    ("Full Time", "Full Time"),
    ("Part Time", "Part Time"),
    ("Internship", "Internship"),
    ("Freelance", "Freelance")
]

class UserProfile(AbstractUser):
    username = models.CharField(max_length=120, unique=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(('password'), max_length=128, help_text=("use'[algo]$[salt]$[hexdigest]'"))
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, null=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.username

class User_Profile_creation(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    title = models.CharField(max_length=100, null=True)
    profile = models.ImageField(null=True)
    description = models.TextField()
    contact = models.IntegerField()
    category = models.CharField(choices=OPTIONS, default="Website & Software",max_length=100)
    resume = models.FileField(null=True)

    def __str__(self) -> str:
        return self.user_profile.username

class Org_Profile_Creation(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    contact = models.IntegerField()
    orgname = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.orgname

class JobPost(models.Model):
    slug = models.SlugField(max_length=255, unique=True, null=True)
    title = models.CharField(max_length=100)
    type = models.CharField(choices=JOBTYPE, default="Full Time", max_length=100)
    location = models.CharField(max_length=100)
    category = models.CharField(choices=OPTIONS, default="Website & Software", max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    created_on = models.DateField(auto_now_add=True)
    organization = models.ForeignKey(Org_Profile_Creation, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(JobPost, self).save(*args, **kwargs)

class Proposal(models.Model):
    jobpost = models.ForeignKey(JobPost, on_delete=models.CASCADE, null=True)
    proposal = models.TextField()
    user = models.ForeignKey(User_Profile_creation, on_delete=models.CASCADE, null=True)

    def __int__(self):
        return self.jobpost