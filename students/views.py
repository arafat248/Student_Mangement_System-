from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from students.models import Student
from students.serializer import student_serila

# Create your views here.
class studentview(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = student_serila