from django.db import models
from datetime import datetime
from apps.users.models import User
from django.utils import timezone


# Create your models here.
class Tests(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False,blank=False,max_length=400)
    create_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return  self.name

class IntentoTest(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    test = models.ForeignKey(Tests,on_delete=models.CASCADE)
    score_total = models.FloatField(blank=False, null=False)
    date = models.DateField(blank=False,null=False, default=timezone.now())
    
    def __str__(self):
        return str(self.id)

class Questions(models.Model):
    id = models.AutoField(primary_key=True)
    test = models.ForeignKey(Tests, on_delete=models.CASCADE)
    description = models.TextField(blank=False, null=False)
    score_question = models.FloatField(blank=False,null=True, default=0)
    

    def __str__(self):
        return self.description

class Answers(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(blank=False, null=False)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    def __str__(self):
        return self.description

class AnswersValidate(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(blank=False, null=False)
    answers = models.ForeignKey(Answers, on_delete=models.CASCADE)
    def __str__(self):
        return self.description

