# Generated by Django 5.0.3 on 2024-06-06 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pri1', '0002_abacus_agriculturalscience_basicscitech_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mathematics',
            new_name='MathematicsScores',
        ),
        migrations.AlterModelOptions(
            name='english',
            options={'verbose_name_plural': 'English'},
        ),
        migrations.AlterModelOptions(
            name='mathematicsscores',
            options={'verbose_name_plural': 'Maths Scores'},
        ),
    ]