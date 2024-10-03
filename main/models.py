from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True, blank=True)
    hemis_id = models.IntegerField(default=0)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    specialty = models.CharField(max_length=255)
    department_id = models.IntegerField(default=0)
    department_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class EduYear(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class StudyPlan(models.Model):
    SEMESTER = (
        ('1', '1-yillik'),
        ('2', '2-yillik'),
    )
    EDU_TYPE = (
        ('M', 'Maruza'),
        ('A', 'Amaliyot'),
        ('S', 'Semestr'),
        ('L', 'Laboratoriya'),
    )
    edu_year = models.ForeignKey(EduYear, on_delete=models.CASCADE, related_name='plan')
    semester = models.CharField(max_length=1, choices=SEMESTER, default='1')
    edu_type = models.CharField(max_length=1, choices=EDU_TYPE, default='M')
    subject_name = models.TextField(blank=True, null=True)
    hour = models.IntegerField(default=0)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plan')
    groups = models.TextField(blank=True, null=True)
    group_division = models.BooleanField(default=False)
    thread = models.BooleanField(default=False)
    confirm = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject_name


class LessonSchedule(models.Model):
    SEMESTER = (
        ('1', '1-yillik'),
        ('2', '2-yillik'),
    )
    edu_year = models.ForeignKey(EduYear, on_delete=models.CASCADE, related_name='schedule')
    semester = models.CharField(max_length=1, choices=SEMESTER, default='1')
    date_time = models.DateField()
    study_plan = models.ForeignKey(StudyPlan, on_delete=models.CASCADE, related_name='schedule')
    para = models.IntegerField(default=1)
    group = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='schedule')

    def __str__(self):
        return self.semester

