from django.contrib.auth import authenticate
from .serializers import ProfileSerializer, UserProfileCreationSerializer, OrgProfileCreationSerializer, JobsSerializer, JobPostSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Org_Profile_Creation, JobPost
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


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
            data['status'] = user.status
        else:
            data = serializer.errors
        return Response(data)

@permission_classes((permissions.AllowAny,))
class TokenView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username,password=password)
        serializer = ProfileSerializer(user)
        if user:
            token = Token.objects.get_or_create(user=user)
            return Response({"token": user.auth_token.key, "user": serializer.data})
        else:
            return Response({"error": "Wrong credentials"}, status = status.HTTP_400_BAD_REQUEST)

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

@api_view(['POST',])
@permission_classes((permissions.AllowAny,))
def org_profile(request):
    if request.method == 'POST':
        serializer = OrgProfileCreationSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            org = serializer.save()
            data['response'] = 'success'
            data['user_profile'] = org.user_profile
            data['firstname'] = org.firstname
            data['lastname'] = org.lastname
            data['location'] = org.location
            data['description'] = org.description
            data['contact'] = org.contact
            data['orgname'] = org.orgname
        else:
            data = serializer.errors
        return Response(serializer.data)

@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def jobpost(request):
    if request.user.is_authenticated:
        cur_org = get_object_or_404(Org_Profile_Creation, user_profile=request.user)
        org = cur_org.orgname
        if request.method == 'POST':
            serializer = JobPostSerializer(data=request.data)
            data = {}

            if serializer.is_valid():
                job = serializer.save()
                data['response'] = 'success'
                data['type'] = job.type
                data['location'] = job.location
                data['category'] = job.category
                data['description'] = job.description
                data['title'] = job.title
                data['organization'] = org
            else:
                data = serializer.errors
            return Response(data)

class Organizations(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = JobsSerializer

    def get_queryset(self):
        return JobPost.objects.all()
