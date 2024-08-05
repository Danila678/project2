from django.shortcuts import render, get_object_or_404
from .models import Course, Module

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'course_detail.html', {'course': course})

def module_detail(request, module_id):
    module = get_object_or_404(Module, pk=module_id)
    return render(request, 'module_detail.html', {'module': module})
