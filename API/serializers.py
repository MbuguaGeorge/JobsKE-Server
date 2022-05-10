from rest_framework import serializers
from .models import UserProfile, User_Profile_creation

class ProfileSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = UserProfile(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
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