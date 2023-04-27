from django.db import models
from django.urls import reverse;
class Student(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    marks=models.FloatField(max_length=50)
    def __str__(self):
        return self.sname
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})