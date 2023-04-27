from django.contrib import admin
from MyApps1.models import Student
class StudentAdmin(admin.ModelAdmin):
    list_display = ['sno','sname','course','marks']
admin.site.register(Student,StudentAdmin)