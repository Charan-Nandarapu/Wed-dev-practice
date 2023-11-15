from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=50)
    Age=models.IntegerField(max_length=20)

    def __str__(self):
        return self.name



class Course(models.Model):
    courseName = models.CharField(max_length=100,unique=True)
    students=models.ManyToManyField(Student,related_name="courses")

    def __str__(self):
        return self.name
    
    


# Create your models here.
