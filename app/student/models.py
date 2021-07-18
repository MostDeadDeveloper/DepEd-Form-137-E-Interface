from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from core.models import BaseModel

class Student(models.Model):
    LRN = models.CharField(max_length=15, null=True)
    last_name = models.CharField(max_length=15, null=True)
    middle_initial = models.CharField(max_length=1, null=True)
    first_name = models.CharField(max_length=15, null=True)
    division = models.CharField(max_length=15, null=True)
    school = models.CharField(max_length=15, null=True)
    sex = models.CharField(max_length=1, null=True)
    date_of_birth = models.DateField(null=True)
    town = models.CharField(max_length=15, null=True)
    date_of_entrance = models.DateField(null=True)
    parent_id = models.ForeignKey(
        'student.Parent',
        null=True,
        on_delete=models.CASCADE,
    )

class Parent(models.Model):
    parent_name = models.CharField(max_length=15, null=True)
    parent_address = models.CharField(max_length=32, null=True)


class StudentRecord(models.Model):
    # LRN = models.CharField(max_length=15, null=True)
    # grade_level = models.CharField(max_length=15, null=True)
    school_year = models.CharField(max_length=15, null=True)
    school = models.CharField(max_length=15, null=True)
    school_days_count = models.IntegerField(null=True)
    school_days_absent_count  = models.IntegerField(null=True)
    cause_of_absence = models.CharField(max_length=16, null=True)
    school_days_tardiness_count  = models.IntegerField(null=True)
    cause_of_tardiness  = models.IntegerField(max_length=16,null=True)
    school_days_present_count  = models.IntegerField(null=True)


class SubjectRecord(models.Model):
    learning_area = models.CharField(max_length=15, null=True)
    # LRN = models.CharField(max_length=15, null=True)
    # grade_level = models.CharField(max_length=15, null=True)
    first_grading_rating = models.IntegerField(null=True)
    second_grading_rating = models.IntegerField(null=True)
    third_grading_rating = models.IntegerField(null=True)
    fourth_grading_rating = models.IntegerField(null=True)
    remarks = models.CharField(max_length=16, null=True)

class
