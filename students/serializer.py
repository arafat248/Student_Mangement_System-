from  rest_framework import serializers
from students.models import studentmodel

class student_serila(serializers.ModelSerializer):
    class Meta:
        model = studentmodel
        fields = '__all__'