from django.contrib import admin
from .models import Homework, Lesson

# Register your models here.

@admin.register(Homework)
class HomeWorkAdmin(admin.ModelAdmin):
    list_display =('title', 'content', 'deadline', 'created_date')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display=('name',)