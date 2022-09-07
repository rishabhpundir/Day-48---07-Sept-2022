from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

class School(models.Model):
    school_name = models.CharField(max_length=100, null=False, blank=False)
    address = models.TextField()

    def __str__(self):
        return self.school_name

class Class(models.Model):
    class_standard = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(12)])
    section = models.CharField(max_length=1, null=False, blank=False)
    school_name = models.ForeignKey('School', related_name='class_school', on_delete=models.CASCADE)


    def __str__(self):
        return str(self.class_standard) + " " + self.section


class Student(models.Model):
    student_name = models.CharField(max_length=100, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    gender = models.CharField(choices=GENDER, max_length=10, default='GENDER')
    standard = models.ForeignKey('Class', related_name='student_class', on_delete=models.CASCADE)
    school = models.ForeignKey('School', related_name='student_school', on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name

