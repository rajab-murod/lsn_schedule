from django.db import models


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
    teacher_name = models.CharField(max_length=50)
    teacher_id = models.IntegerField(default=0)
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
    semester = models.CharField(max_length=1, choices=SEMESTER, default='1')
    date_time = models.DateField()
    study_plan = models.ForeignKey(StudyPlan, on_delete=models.CASCADE, related_name='schedule')
    para = models.IntegerField(default=1)
    group = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.date_time
