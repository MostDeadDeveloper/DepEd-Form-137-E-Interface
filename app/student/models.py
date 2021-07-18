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
    values = models.ManyToManyField(
        'student.CoreValue',
        through='StudentValue',
        through_fields=('LRN', 'value'),
    )
    subject_records = models.ManyToManyField(
        'student.StudentRecord',
        through='student.SubjectRecord',
        through_fields=('LRN','student_record')
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
    student_record = models.ForeignKey(
        'student.StudentRecord',
        null=True,
        on_delete=models.CASCADE,
    )
    LRN = models.ForeignKey(
        'student.Student',
        null=True,
        on_delete=models.CASCADE,
    )
    learning_area = models.CharField(max_length=15, null=True)
    # LRN = models.CharField(max_length=15, null=True)
    # grade_level = models.CharField(max_length=15, null=True)
    first_grading_rating = models.IntegerField(null=True)
    second_grading_rating = models.IntegerField(null=True)
    third_grading_rating = models.IntegerField(null=True)
    fourth_grading_rating = models.IntegerField(null=True)
    remarks = models.CharField(max_length=16, null=True)


class CoreValue(models.Model):
    value_name = models.CharField(max_length=16, null=True)
    behavior_description = models.CharField(max_length=32, null=True)


class StudentValue(models.Model):
    LRN = models.ForeignKey(
        'student.Student',
        null=True,
        on_delete=models.CASCADE,
    )
    value = models.ForeignKey(
        'student.CoreValue',
        null=True,
        on_delete=models.CASCADE,
    )
    # grade_level = models.CharField(max_length=15, null=True)
    first_grading_rating = models.IntegerField(null=True)
    second_grading_rating = models.IntegerField(null=True)
    third_grading_rating = models.IntegerField(null=True)
    fourth_grading_rating = models.IntegerField(null=True)


class Certificate(models.Model):
    # LRN = models.CharField(max_length=15, null=True)
    next_grade = models.CharField(max_length=10, null=True)
    # signature
    date = models.DateField(null=True)
    designation = models.CharField(max_length=16, null=True)
