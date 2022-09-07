from django.contrib import admin
from .models import School, Class, Student
# Register your models here.

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['school_name', 'address']

@admin.register(Class)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['class_standard', 'section', 'school_name']

@admin.register(Student)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'age', 'gender', 'standard', 'school']
