from django.contrib import admin
from .models import Course
# Register your models here.

class course(admin.ModelAdmin):
    list_display=("Name","Email","Password")

admin.site.register(Course,course)
