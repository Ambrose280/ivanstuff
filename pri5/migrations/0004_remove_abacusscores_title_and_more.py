# Generated by Django 5.0.3 on 2024-06-08 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pri5', '0003_abacusscores_classorhomework_abacusscores_exams_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abacusscores',
            name='title',
        ),
        migrations.RemoveField(
            model_name='agriculturalsciencescores',
            name='title',
        ),
        migrations.RemoveField(
            model_name='basicscitechscores',
            name='title',
        ),
        migrations.RemoveField(
            model_name='civiceducationscores',
            name='title',
        ),
        migrations.RemoveField(
            model_name='computerstudiesscores',
            name='title',
        ),
        migrations.RemoveField(
            model_name='creativeartsscores',
            name='title',
        ),
        migrations.RemoveField(
            model_name='creativewritingscores',
            name='title',
        ),
        migrations.RemoveField(
            model_name='crkscores',
            name='title',
        ),
        migrations.RemoveField(
            model_name='englishliteraturescores',
            name='title',
        ),
        migrations.RemoveField(
            model_name='englishscores',
            name='title',
        ),
        migrations.RemoveField(
            model_name='historyscores',
            name='title',
        ),
        migrations.RemoveField(
            model_name='mathematicsscores',
            name='title',
        ),
        migrations.RemoveField(
            model_name='musicscores',
            name='title',
        ),
        migrations.RemoveField(
            model_name='phescores',
            name='title',
        ),
        migrations.RemoveField(
            model_name='quantitativereasoningscores',
            name='title',
        ),
        migrations.RemoveField(
            model_name='socialstudiesscores',
            name='title',
        ),
        migrations.RemoveField(
            model_name='spellingsscores',
            name='title',
        ),
        migrations.RemoveField(
            model_name='verbalreasoningscores',
            name='title',
        ),
    ]
