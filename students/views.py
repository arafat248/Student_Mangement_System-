from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from students.models import studentmodel
from students.serializer import student_serila

# Create your views here.
class students_view(ModelViewSet):
    queryset = studentmodel.objects.all()
    serializer_class = student_serila