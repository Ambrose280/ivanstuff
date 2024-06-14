from django.db import models

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Null', 'Null')
         )

CLASS = (
    ('Primary 5', 'Primary 5'),
    ('Primary 4', 'Primary 4'),
    ('Primary 3', 'Primary 3'),
    ('Primary 2', 'Primary 2'),
    ('Primary 1', 'Primary 1'),
    ('Nursery 2', 'Nursery 2'),
    ('Nursery 1', 'Nursery 1'),
    ('Pre-nursery', 'Pre-nursery'),
    ('Creche', 'Creche'),
)
# Create your models here.
class Pupil(models.Model):
    firstname = models.CharField(default='firstname', null=True, blank=True, max_length=256)
    middlename = models.CharField(default='middlename', null=True, blank=True, max_length=256)
    surname = models.CharField(default='surname', null=True, blank=True, max_length=256)
    address = models.CharField(default='null', null=True, blank=True, max_length=256)
    gender = models.CharField(choices=GENDER, max_length=50, default="Null")
    classlevel = models.CharField(choices=CLASS, max_length=50, default="Primary 5")

    def __str__(self):
        return self.firstname