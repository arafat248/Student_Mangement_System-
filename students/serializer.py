from  rest_framework import serializers
from students.models import student

class student_serila(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'