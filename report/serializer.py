from rest_framework import serializers

class report_serial(serializers.Serializer):
    name = serializers.CharField()
    roll = serializers.IntegerField()
    class_name = serializers.CharField()
    average_marks = serializers.FloatField()
    grade = serializers.CharField()
    subjects = serializers.ListField()
