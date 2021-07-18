from django.contrib import admin

# Register your models here.

from core import admin as core_admin
from .models import (
    Student,
    Parent,
    StudentRecord,
    StudentValue,
    SubjectRecord,
    CoreValue,
    Certificate,
)


class StudentRecordInline(admin.TabularInline):
    model = StudentRecord
    fields = (
        'school_year',
        'school',
    )

class SubjectRecordInline(admin.TabularInline):
    model = SubjectRecord
    fields = (
        'student_record',
        'learning_area',
        'first_grading_rating',
        'second_grading_rating',
        'third_grading_rating',
        'fourth_grading_rating',
        'remarks',
    )

class StudentValueInline(admin.TabularInline):
    model = StudentValue
    fields = (
        'value',
        'first_grading_rating',
        'second_grading_rating',
        'third_grading_rating',
        'fourth_grading_rating',
    )

class StudentAdmin(core_admin.AuditModelAdmin):
    inlines = (SubjectRecordInline,StudentValueInline,)


class StudentRecordAdmin(core_admin.AuditModelAdmin):
    inlines = (SubjectRecordInline,)

admin.site.register(Student,StudentAdmin)
admin.site.register(Parent)
admin.site.register(SubjectRecord)
admin.site.register(StudentRecord, StudentRecordAdmin)
admin.site.register(CoreValue)
admin.site.register(StudentValue)
admin.site.register(Certificate)
