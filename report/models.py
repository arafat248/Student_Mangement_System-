from django.db import models

class Report(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    class_name = models.CharField(max_length=50)
    average_marks = models.FloatField()
    grade = models.FloatField()


    def __str__(self):
        return self.name