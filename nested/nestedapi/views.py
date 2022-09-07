from logging import raiseExceptions
from .models import School, Class, Student
from .serializers import RegisterSerializer, StudentSerializer, ClassSerializer, SchoolSerializer, User
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

# Create your views here.

class SchoolView(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

class ClassView(ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
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


    