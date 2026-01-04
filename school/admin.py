from django.contrib import admin
from .models import Student, Teacher, Course

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_number', 'email')
    search_fields = ('name', 'roll_number', 'email')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email')
    search_fields = ('name', 'subject')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')
    search_fields = ('name',)
    list_filter = ('teacher',)
