from django.db import models

# Create your models here.
class studentmodel(models.Model):
    name = models.CharField(max_length=50)
    roll = models.PositiveIntegerField()
    intake = models.PositiveIntegerField()
    section = models.PositiveIntegerField()
    program = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name