from django.db import models

# Create your models here.
class MathematicsScores(models.Model):
    title = models.CharField(max_length=50, verbose_name="Mathematics Scores")
    class Meta:
        verbose_name_plural = "Maths Scores"

class EnglishScores(models.Model):
    title = models.CharField(max_length=50, verbose_name="English Language")
    class Meta:
        verbose_name_plural = "English Scores"
    
class EnglishLiteratureScores(models.Model):
    title = models.CharField(max_length=50, verbose_name="Literature Scores")
    class Meta:
        verbose_name_plural = "English Literature Scores"

class BasicSciTechScores(models.Model):
    title = models.CharField(max_length=50, verbose_name="Basic Science & Tech")
    class Meta:
        verbose_name_plural = "Basic Science/Tech Scores"
    
class ComputerStudiesScores(models.Model):
    title = models.CharField(max_length=50, verbose_name="Computer Studies Scores")
    class Meta:
        verbose_name_plural = "Computer Studies Scores"

class PHEScores(models.Model):
    title = models.CharField(max_length=50, verbose_name="Physical & Health Education Scores")
    class Meta:
        verbose_name_plural = "PHE Scores"
    
class AgriculturalScienceScores(models.Model):
    title = models.CharField(max_length=50, verbose_name="Agricultural Science Scores")
    class Meta:
        verbose_name_plural = "Agric Scores"

class SocialStudiesScores(models.Model):
    title = models.CharField(max_length=50, verbose_name="Social Studies")
    class Meta:
        verbose_name_plural = "Social Studies Scores"
    
class CivicEducationScores(models.Model):
    title = models.CharField(max_length=50, verbose_name="Civic Education Scores")
    class Meta:
        verbose_name_plural = "Civic Education Scores"

class CRKScores(models.Model):
    title = models.CharField(max_length=50, verbose_name="CRK Scores")
    class Meta:
        verbose_name_plural = "CRK Scores"
    
class CreativeArtsScores(models.Model):
    title = models.CharField(max_length=50, verbose_name="Creative Arts Scores")
    class Meta:
        verbose_name_plural = "Creative Arts Scores"

class CreativeWritingScores(models.Model):
    title = models.CharField(max_length=50, verbose_name="Creative Writing Scores")
    class Meta:
        verbose_name_plural = "Creative Writing Scores"
    
class AbacusScores(models.Model):
    title = models.CharField(max_length=50, verbose_name="Abacus Scores")
    class Meta:
        verbose_name_plural = "Abacus Scores"

class SpellingsScores(models.Model):
    title = models.CharField(max_length=50, verbose_name="Spellings Scores")
    class Meta:
        verbose_name_plural = "Spellings Scores"

class VerbalReasoningScores(models.Model):
    title = models.CharField(max_length=50, verbose_name="Verbal Reasoning Scores")
    class Meta:
        verbose_name_plural = "Verbal Reasoning Scores"

class QuantitativeReasoningScores(models.Model):
    title = models.CharField(max_length=50, verbose_name="Quantitative Reasoning Scores")
    class Meta:
        verbose_name_plural = "Quantitative Reasoning Scores"
    
class HistoryScores(models.Model):
    title = models.CharField(max_length=50, verbose_name="History Scores")
    class Meta:
        verbose_name_plural = "History Scores"

class MusicScores(models.Model):
    title = models.CharField(max_length=50, verbose_name="Music Scores")
    class Meta:
        verbose_name_plural = "Music Scores"
