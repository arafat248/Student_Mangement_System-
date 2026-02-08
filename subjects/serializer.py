from rest_framework import serializers
from subjects.models import Subject

class subject_serial(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"
        
