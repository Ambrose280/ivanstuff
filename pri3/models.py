from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from pupilbase.models import Pupil
class MathematicsScores(models.Model):
    pupil = models.ForeignKey(Pupil, verbose_name="Pupil", null=True, on_delete=models.CASCADE, related_name='p3mathpupil')
    test1 = models.PositiveIntegerField(default=0, null=True, blank=True)
    test2 = models.PositiveIntegerField(default=0, null=True, blank=True)
    classorhomework = models.PositiveIntegerField(default=0, null=True, blank=True)
    exams = models.PositiveIntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.pupil.firstname
    class Meta:
        verbose_name_plural = "Maths Scores"

class EnglishScores(models.Model):
    pupil = models.ForeignKey(Pupil, verbose_name="Pupil", null=True, on_delete=models.CASCADE, related_name='p3engpupil')
    test1 = models.PositiveIntegerField(default=0, null=True, blank=True)
    test2 = models.PositiveIntegerField(default=0, null=True, blank=True)
    classorhomework = models.PositiveIntegerField(default=0, null=True, blank=True)
    exams = models.PositiveIntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.pupil.firstname
    class Meta:
        verbose_name_plural = "English Scores"
    
class EnglishLiteratureScores(models.Model):
    pupil = models.ForeignKey(Pupil, verbose_name="Pupil", null=True, on_delete=models.CASCADE, related_name='p3literaturepupil')
    test1 = models.PositiveIntegerField(default=0, null=True, blank=True)
    test2 = models.PositiveIntegerField(default=0, null=True, blank=True)
    classorhomework = models.PositiveIntegerField(default=0, null=True, blank=True)
    exams = models.PositiveIntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.pupil.firstname
    class Meta:
        verbose_name_plural = "English Literature Scores"

class BasicSciTechScores(models.Model):
    pupil = models.ForeignKey(Pupil, verbose_name="Pupil", null=True, on_delete=models.CASCADE, related_name='p3scitechpupil')
    test1 = models.PositiveIntegerField(default=0, null=True, blank=True)
    test2 = models.PositiveIntegerField(default=0, null=True, blank=True)
    classorhomework = models.PositiveIntegerField(default=0, null=True, blank=True)
    exams = models.PositiveIntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.pupil.firstname
    class Meta:
        verbose_name_plural = "Basic Science/Tech Scores"
    
class ComputerStudiesScores(models.Model):
    pupil = models.ForeignKey(Pupil, verbose_name="Pupil", null=True, on_delete=models.CASCADE, related_name='p3cspupil')
    test1 = models.PositiveIntegerField(default=0, null=True, blank=True)
    test2 = models.PositiveIntegerField(default=0, null=True, blank=True)
    classorhomework = models.PositiveIntegerField(default=0, null=True, blank=True)
    exams = models.PositiveIntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.pupil.firstname
    class Meta:
        verbose_name_plural = "Computer Studies Scores"

class PHEScores(models.Model):
    pupil = models.ForeignKey(Pupil, verbose_name="Pupil", null=True, on_delete=models.CASCADE, related_name='p3phepupil')
    test1 = models.PositiveIntegerField(default=0, null=True, blank=True)
    test2 = models.PositiveIntegerField(default=0, null=True, blank=True)
    classorhomework = models.PositiveIntegerField(default=0, null=True, blank=True)
    exams = models.PositiveIntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.pupil.firstname
    class Meta:
        verbose_name_plural = "PHE Scores"
    
class AgriculturalScienceScores(models.Model):
    pupil = models.ForeignKey(Pupil, verbose_name="Pupil", null=True, on_delete=models.CASCADE, related_name='p3agricpupil')
    test1 = models.PositiveIntegerField(default=0, null=True, blank=True)
    test2 = models.PositiveIntegerField(default=0, null=True, blank=True)
    classorhomework = models.PositiveIntegerField(default=0, null=True, blank=True)
    exams = models.PositiveIntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.pupil.firstname
    class Meta:
        verbose_name_plural = "Agric Scores"

class SocialStudiesScores(models.Model):
    pupil = models.ForeignKey(Pupil, verbose_name="Pupil", null=True, on_delete=models.CASCADE, related_name='p3socialpupil')
    test1 = models.PositiveIntegerField(default=0, null=True, blank=True)
    test2 = models.PositiveIntegerField(default=0, null=True, blank=True)
    classorhomework = models.PositiveIntegerField(default=0, null=True, blank=True)
    exams = models.PositiveIntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.pupil.firstname
    class Meta:
        verbose_name_plural = "Social Studies Scores"
    
class CivicEducationScores(models.Model):
    pupil = models.ForeignKey(Pupil, verbose_name="Pupil", null=True, on_delete=models.CASCADE, related_name='p3civicpupil')
    test1 = models.PositiveIntegerField(default=0, null=True, blank=True)
    test2 = models.PositiveIntegerField(default=0, null=True, blank=True)
    classorhomework = models.PositiveIntegerField(default=0, null=True, blank=True)
    exams = models.PositiveIntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.pupil.firstname
    class Meta:
        verbose_name_plural = "Civic Education Scores"

class CRKScores(models.Model):
    pupil = models.ForeignKey(Pupil, verbose_name="Pupil", null=True, on_delete=models.CASCADE, related_name='p3crkpupil')
    test1 = models.PositiveIntegerField(default=0, null=True, blank=True)
    test2 = models.PositiveIntegerField(default=0, null=True, blank=True)
    classorhomework = models.PositiveIntegerField(default=0, null=True, blank=True)
    exams = models.PositiveIntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.pupil.firstname
    class Meta:
        verbose_name_plural = "CRK Scores"
    
class CreativeArtsScores(models.Model):
    pupil = models.ForeignKey(Pupil, verbose_name="Pupil", null=True, on_delete=models.CASCADE, related_name='p3artspupil')
    test1 = models.PositiveIntegerField(default=0, null=True, blank=True)
    test2 = models.PositiveIntegerField(default=0, null=True, blank=True)
    classorhomework = models.PositiveIntegerField(default=0, null=True, blank=True)
    exams = models.PositiveIntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.pupil.firstname
    class Meta:
        verbose_name_plural = "Creative Arts Scores"

class CreativeWritingScores(models.Model):
    pupil = models.ForeignKey(Pupil, verbose_name="Pupil", null=True, on_delete=models.CASCADE, related_name='p3writingpupil')
    test1 = models.PositiveIntegerField(default=0, null=True, blank=True)
    test2 = models.PositiveIntegerField(default=0, null=True, blank=True)
    classorhomework = models.PositiveIntegerField(default=0, null=True, blank=True)
    exams = models.PositiveIntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.pupil.firstname
    class Meta:
        verbose_name_plural = "Creative Writing Scores"
    
class AbacusScores(models.Model):
    pupil = models.ForeignKey(Pupil, verbose_name="Pupil", null=True, on_delete=models.CASCADE, related_name='p3abacuspupil')
    test1 = models.PositiveIntegerField(default=0, null=True, blank=True)
    test2 = models.PositiveIntegerField(default=0, null=True, blank=True)
    classorhomework = models.PositiveIntegerField(default=0, null=True, blank=True)
    exams = models.PositiveIntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.pupil.firstname
    class Meta:
        verbose_name_plural = "Abacus Scores"

class SpellingsScores(models.Model):
    pupil = models.ForeignKey(Pupil, verbose_name="Pupil", null=True, on_delete=models.CASCADE, related_name='p3spellingpupil')
    test1 = models.PositiveIntegerField(default=0, null=True, blank=True)
    test2 = models.PositiveIntegerField(default=0, null=True, blank=True)
    classorhomework = models.PositiveIntegerField(default=0, null=True, blank=True)
    exams = models.PositiveIntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.pupil.firstname
    class Meta:
        verbose_name_plural = "Spellings Scores"

class VerbalReasoningScores(models.Model):
    pupil = models.ForeignKey(Pupil, verbose_name="Pupil", null=True, on_delete=models.CASCADE, related_name='p3verbalpupil')
    test1 = models.PositiveIntegerField(default=0, null=True, blank=True)
    test2 = models.PositiveIntegerField(default=0, null=True, blank=True)
    classorhomework = models.PositiveIntegerField(default=0, null=True, blank=True)
    exams = models.PositiveIntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.pupil.firstname
    class Meta:
        verbose_name_plural = "Verbal Reasoning Scores"

class QuantitativeReasoningScores(models.Model):
    pupil = models.ForeignKey(Pupil, verbose_name="Pupil", null=True, on_delete=models.CASCADE, related_name='p3quantpupil')
    test1 = models.PositiveIntegerField(default=0, null=True, blank=True)
    test2 = models.PositiveIntegerField(default=0, null=True, blank=True)
    classorhomework = models.PositiveIntegerField(default=0, null=True, blank=True)
    exams = models.PositiveIntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.pupil.firstname
    class Meta:
        verbose_name_plural = "Quantitative Reasoning Scores"
    
class HistoryScores(models.Model):
    pupil = models.ForeignKey(Pupil, verbose_name="Pupil", null=True, on_delete=models.CASCADE, related_name='p3historypupil')
    test1 = models.PositiveIntegerField(default=0, null=True, blank=True)
    test2 = models.PositiveIntegerField(default=0, null=True, blank=True)
    classorhomework = models.PositiveIntegerField(default=0, null=True, blank=True)
    exams = models.PositiveIntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.pupil.firstname
    class Meta:
        verbose_name_plural = "History Scores"

class MusicScores(models.Model):
    pupil = models.ForeignKey(Pupil, verbose_name="Pupil", null=True, on_delete=models.CASCADE, related_name='p3musicpupil')
    test1 = models.PositiveIntegerField(default=0, null=True, blank=True)
    test2 = models.PositiveIntegerField(default=0, null=True, blank=True)
    classorhomework = models.PositiveIntegerField(default=0, null=True, blank=True)
    exams = models.PositiveIntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.pupil.firstname
    class Meta:
        verbose_name_plural = "Music Scores"
    