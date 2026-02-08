from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=8)

    def __str__(self):
        return self.name