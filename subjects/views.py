from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from subjects.models import Subject
from subjects.serializer import subject_serial

# Create your views here.
class subjectview(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = subject_serial
