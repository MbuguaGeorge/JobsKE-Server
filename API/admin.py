from django.contrib import admin
from .models import UserProfile, User_Profile_creation, Org_Profile_Creation

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(User_Profile_creation)
admin.site.register(Org_Profile_Creation)