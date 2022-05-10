from rest_framework.serializers import Serializer
from .serializers import ProfileSerializer, UserProfileCreationSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response

# Create your views here.
@api_view(['POST',])
@permission_classes((permissions.AllowAny,))
def register(request):
    if request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'success'
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data)

@api_view(['POST',])
@permission_classes((permissions.AllowAny,))
def create_profile(request):
    if request.method == 'POST':
        serializer = UserProfileCreationSerializer(data=request.data)
        data= {}

        if serializer.is_valid():
            prof = serializer.save()
            data['response'] = 'success'
            data['user_profile'] = prof.user_profile
            data['firstname'] = prof.firstname
            data['lastname'] = prof.lastname
            data['profile'] = prof.profile
            data['description'] = prof.description
            data['contact'] = prof.contact
            data['category'] = prof.category
            data['resume'] = prof.resume
        else:
            data = serializer.errors
        return Response(serializer.data)