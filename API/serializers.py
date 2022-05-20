from rest_framework import serializers
from .models import UserProfile, User_Profile_creation, Org_Profile_Creation, JobPost

class ProfileSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'status','password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = UserProfile(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            status = self.validated_data['status'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password' : 'passwords do not match'})
        user.set_password(password)
        user.save()
        return user


class UserProfileCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Profile_creation
        fields = ('user_profile','firstname','lastname','profile','description','contact','category','resume')
        
    def save(self):
        profile = User_Profile_creation(
            user_profile = self.validated_data['user_profile'],
            firstname = self.validated_data['firstname'],
            lastname = self.validated_data['lastname'],
            profile = self.validated_data['profile'],
            description = self.validated_data['description'],
            contact = self.validated_data['contact'],
            category = self.validated_data['category'],
            resume = self.validated_data['resume']
        )

        profile.save()
        return profile

class OrgProfileCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Org_Profile_Creation
        fields = ('user_profile', 'firstname', 'lastname', 'contact', 'orgname', 'description', 'location')

    def save(self):
        org = Org_Profile_Creation(
            user_profile = self.validated_data['user_profile'],
            firstname = self.validated_data['firstname'],
            lastname = self.validated_data['lastname'],
            contact = self.validated_data['contact'],
            orgname = self.validated_data['orgname'],
            description = self.validated_data['description'],
            location = self.validated_data['location']
        )

        org.save()
        return org

class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = ('type', 'location', 'category', 'description', 'title')

    def save(self):
        job = JobPost(
            type = self.validated_data['type'],
            location = self.validated_data['location'],
            category = self.validated_data['category'],
            description = self.validated_data['description'],
            title = self.validated_data['title'],
            #organization = self.validated_data['organization']
        )

        job.save()
        return job

class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = ('type', 'location', 'category', 'description', 'title', 'organization')