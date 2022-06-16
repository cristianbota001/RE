from django.db import models
from django.contrib.auth.models import User

class Subjects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject_name = models.TextField()

    def __str__(self):
        return self.subject_name + "_" + self.user.username

class Grades(models.Model):
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    grade = models.FloatField()
    if_average = models.BooleanField()

    def __str__(self):
        return self.subject.subject_name + "_" + str(self.grade) + "_" +  self.subject.user.username
