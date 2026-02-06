from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from students.models import student
from students.serializer import student_serila

# Create your views here.
class students_view(ModelViewSet):
    queryset = student.objects.all()
    serializer_class = student_serila