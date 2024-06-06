from django.db import models

# Create your models here.
class Mathematics(models.Model):
    title = models.CharField(max_length=50, verbose_name="Mathematics")

class English(models.Model):
    title = models.CharField(max_length=50, verbose_name="English Language")
    
class EnglishLiterature(models.Model):
    title = models.CharField(max_length=50, verbose_name="Literature-In-English")

class BasicSciTech(models.Model):
    title = models.CharField(max_length=50, verbose_name="Basic Science & Tech")
    
class ComputerStudies(models.Model):
    title = models.CharField(max_length=50, verbose_name="Computer Studies")

class PHE(models.Model):
    title = models.CharField(max_length=50, verbose_name="Physical & Health Education")
    
class AgriculturalScience(models.Model):
    title = models.CharField(max_length=50, verbose_name="Agricultural Science")

class SocialStudies(models.Model):
    title = models.CharField(max_length=50, verbose_name="Social Studies")
    
class CivicEducation(models.Model):
    title = models.CharField(max_length=50, verbose_name="Civic Education")

class CRK(models.Model):
    title = models.CharField(max_length=50, verbose_name="Christian Religious Knowledge")
    
class CreativeArts(models.Model):
    title = models.CharField(max_length=50, verbose_name="Creative Arts")

class CreativeWriting(models.Model):
    title = models.CharField(max_length=50, verbose_name="Creative Handwriting")
    
class Abacus(models.Model):
    title = models.CharField(max_length=50, verbose_name="Abacus")

class Spellings(models.Model):
    title = models.CharField(max_length=50, verbose_name="Spellings")

class VerbalReasoning(models.Model):
    title = models.CharField(max_length=50, verbose_name="Verbal Reasoning")

class QuantitativeReasoning(models.Model):
    title = models.CharField(max_length=50, verbose_name="Quantitative Reasoning")
    
class History(models.Model):
    title = models.CharField(max_length=50, verbose_name="History")

class Music(models.Model):
    title = models.CharField(max_length=50, verbose_name="Music")
    