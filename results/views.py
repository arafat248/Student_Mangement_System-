from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from results.serializer import result_serial
from results.models import Result

# Create your views here.
class result_view(ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = result_serial