from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name

class Teacher(models.Model):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(
        Company, related_name="teachers", on_delete=models.CASCADE
    )
    students = models.ManyToManyField('Student', related_name="teachers")

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    def get_students(self):
        more_than = 5
        students = self.students.all()
        students_count = students.count()
        
        if students_count == 0:
            return "No students"
        elif students_count < more_than:
            students_names = ", ".join([student.student.first_name for student in students])
            return students_names
        else:
            return f"(More than {more_than} students)"

    def __str__(self):
        return f"{self.teacher.first_name} at {self.company.name} with students: {self.get_students()}"


class Student(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    enrolled_companies = models.ManyToManyField(Company, related_name="students")
    current_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def get_enrolled(self):
        company_names = ", ".join(
            [company.name for company in self.enrolled_companies.all()]
        )
        if len(self.enrolled_companies.all()) < 5:
            return company_names
        else:
            return "Enrolled at 5+ courses"

    def __str__(self):
        return f"{self.student.first_name} at {self.get_enrolled()}"
