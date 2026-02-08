from rest_framework import serializers
from report.models import Report

class report_serial(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
