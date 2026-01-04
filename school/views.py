
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student, Teacher, Course

def home(request):
    return render(request, 'school/home.html')

# Student Views
class StudentListView(ListView):
    model = Student
    template_name = 'school/student_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'school/student_detail.html'
    context_object_name = 'student'

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'roll_number', 'email']
    template_name = 'school/student_form.html'
    success_url = reverse_lazy('student_list')

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'roll_number', 'email']
    template_name = 'school/student_form.html'
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'school/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')

# Teacher Views
class TeacherListView(ListView):
    model = Teacher
    template_name = 'school/teacher_list.html'
    context_object_name = 'teachers'

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'school/teacher_detail.html'
    context_object_name = 'teacher'

class TeacherCreateView(CreateView):
    model = Teacher
    fields = ['name', 'subject', 'email']
    template_name = 'school/teacher_form.html'
    success_url = reverse_lazy('teacher_list')

class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = ['name', 'subject', 'email']
    template_name = 'school/teacher_form.html'
    success_url = reverse_lazy('teacher_list')

class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'school/teacher_confirm_delete.html'
    success_url = reverse_lazy('teacher_list')

# Course Views
class CourseListView(ListView):
    model = Course
    template_name = 'school/course_list.html'
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'school/course_detail.html'
    context_object_name = 'course'

class CourseCreateView(CreateView):
    model = Course
    fields = ['name', 'description', 'teacher', 'students']
    template_name = 'school/course_form.html'
    success_url = reverse_lazy('course_list')

class CourseUpdateView(UpdateView):
    model = Course
    fields = ['name', 'description', 'teacher', 'students']
    template_name = 'school/course_form.html'
    success_url = reverse_lazy('course_list')

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'school/course_confirm_delete.html'
    success_url = reverse_lazy('course_list')
