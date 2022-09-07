from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from .models import Person, RateLimit
from . serializers import PersonSerializer, RegisterSerializer

# Create your views here.

class PersonView(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request,*args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
        "user": 'new user registered successfully!',
        })

