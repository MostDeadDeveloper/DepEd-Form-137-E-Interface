from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from core.models import BaseModel

GRADE_LEVEL_CHOICES = (
    ('Grade I','Grade I',),
    ('Grade II','Grade II',),
    ('Grade III','Grade III',),
    ('Grade IV','Grade IV',),
    ('Grade V','Grade V',),
    ('Grade VI','Grade VI',),
)

class Student(models.Model):
    LRN = models.CharField(
        max_length=14,
        unique=True,
        null=True,
    )
    last_name = models.CharField(max_length=15)
    middle_initial = models.CharField(
        max_length=1,
        blank=True,
        null=True,
    )
    first_name = models.CharField(
        max_length=15,
    )
    division = models.CharField(
        max_length=15,
    )
    school = models.CharField(
        max_length=60
    )
    sex = models.CharField(max_length=1)
    date_of_birth = models.DateField(null=True)
    town = models.CharField(max_length=15)
    date_of_entrance = models.DateField(null=True,blank=True)
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

class Parent(models.Model):
    parent_name = models.CharField(max_length=15, null=True)
    parent_address = models.CharField(max_length=32, null=True)


class StudentRecord(models.Model):
    student = models.ForeignKey(
        'student.Student',
        null=True,
        on_delete=models.CASCADE,
    )
    # LRN = models.CharField(max_length=15, null=True)
    grade_level = models.CharField(choices=GRADE_LEVEL_CHOICES, max_length=9, unique=True)
    school_year = models.CharField(max_length=15)
    school = models.CharField(max_length=64)
    school_days_count = models.IntegerField(default=0,blank=True)
    school_days_absent_count  = models.IntegerField(default=0,blank=True)
    cause_of_absence = models.TextField(max_length=30, null=True,blank=True)
    school_days_tardiness_count  = models.IntegerField(default=0,blank=True)
    cause_of_tardiness  = models.TextField(max_length=30,null=True,blank=True)
    school_days_present_count  = models.IntegerField(default=0,blank=True)
    eligible_for_admission_to_grade = models.CharField(max_length=10, blank=True)


class SubjectRecord(models.Model):
    REMARKS_CHOICES = (
        ('PASSED','PASSED',),
        ('FAILED','FAILED',),
        ('INCOMPLETE','INCOMPLETE',),
    )
    student_record = models.ForeignKey(
        'student.StudentRecord',
        null=True,
        on_delete=models.CASCADE,
    )
    subject = models.ForeignKey(
        'student.Subject',
        on_delete=models.CASCADE,
    )
    first_grading_rating = models.IntegerField(
        null=True,
        validators=[
            MinValueValidator(75),
            MaxValueValidator(100),
        ],
        blank=True,
    )
    second_grading_rating = models.IntegerField(
        null=True,
        validators=[
            MinValueValidator(75),
            MaxValueValidator(100),
        ],
        blank=True,
    )
    third_grading_rating = models.IntegerField(
        null=True,
        validators=[
            MinValueValidator(75),
            MaxValueValidator(100),
        ],
        blank=True,
    )
    fourth_grading_rating = models.IntegerField(
        null=True,
        validators=[
            MinValueValidator(75),
            MaxValueValidator(100),
        ],
        blank=True,
    )
    remarks = models.CharField(
        choices=REMARKS_CHOICES,
        max_length=16,
        null=True,
        blank=True,
    )


class Subject(models.Model):
    learning_area = models.CharField(max_length=15, null=True)


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
    grade_level = models.CharField(choices=GRADE_LEVEL_CHOICES, max_length=9, null=True)
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
