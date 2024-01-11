from django.db import models

from django.core import validators

from django import forms

# Create your models here.

def validation_for_s(data):
    if data.lower()[0].startswith('s'):
        raise forms.ValidationError('Invalid data..')



class Student(models.Model):
    Sname=models.CharField(max_length=100,primary_key=True,validators=[validation_for_s])
    Sage=models.IntegerField()
    Smobile=models.CharField(max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])


    def __str__(self):
        return self.Sname
