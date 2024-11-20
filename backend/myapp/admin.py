from django.contrib import admin
from .models import Company, Teacher, Student


class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "owner")
    search_fields = ("name", "owner__first_name")

    def name(self, obj):
        return obj.name

    name.short_description = "Company Name"


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("teacher", "company", "students_count", "get_students")
    search_fields = (
        "teacher__first_name",
        "company__name",
    )
    list_filter = ("company",)
    ordering = ("teacher__first_name",)

    def students_count(self, obj):
        return obj.students.count()

    students_count.short_description = "Number of Students"  # Change the column title

    def get_students(self, obj):
        return obj.get_students()

    get_students.short_description = "Student List"

class StudentAdmin(admin.ModelAdmin):
    list_display = ("student", "get_enrolled", "current_teacher_name")
    search_fields = (
        "student__first_name",
        "student__last_name",  
    )
    list_filter = ("current_teacher",)
    ordering = ("student__first_name",)

    def current_teacher_name(self, obj):
        return obj.current_teacher.teacher.first_name

    def get_enrolled(self, obj):
        return obj.get_enrolled()

    get_enrolled.short_description = "Enrolled at"



admin.site.register(Company, CompanyAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
