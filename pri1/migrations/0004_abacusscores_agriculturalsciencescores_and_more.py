# Generated by Django 5.0.3 on 2024-06-06 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pri1', '0003_rename_mathematics_mathematicsscores_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbacusScores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Abacus Scores')),
            ],
            options={
                'verbose_name_plural': 'Abacus Scores',
            },
        ),
        migrations.CreateModel(
            name='AgriculturalScienceScores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Agricultural Science Scores')),
            ],
            options={
                'verbose_name_plural': 'Agric Scores',
            },
        ),
        migrations.CreateModel(
            name='CivicEducationScores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Civic Education Scores')),
            ],
            options={
                'verbose_name_plural': 'Civic Education Scores',
            },
        ),
        migrations.CreateModel(
            name='ComputerStudiesScores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Computer Studies Scores')),
            ],
            options={
                'verbose_name_plural': 'Computer Studies Scores',
            },
        ),
        migrations.CreateModel(
            name='CreativeArtsScores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Creative Arts Scores')),
            ],
            options={
                'verbose_name_plural': 'Creative Arts Scores',
            },
        ),
        migrations.CreateModel(
            name='CreativeWritingScores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Creative Writing Scores')),
            ],
            options={
                'verbose_name_plural': 'Creative Writing Scores',
            },
        ),
        migrations.CreateModel(
            name='CRKScores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='CRK Scores')),
            ],
            options={
                'verbose_name_plural': 'CRK Scores',
            },
        ),
        migrations.CreateModel(
            name='EnglishLiteratureScores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Literature Scores')),
            ],
            options={
                'verbose_name_plural': 'English Literature Scores',
            },
        ),
        migrations.CreateModel(
            name='HistoryScores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='History Scores')),
            ],
            options={
                'verbose_name_plural': 'History Scores',
            },
        ),
        migrations.CreateModel(
            name='MusicScores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Music Scores')),
            ],
            options={
                'verbose_name_plural': 'Music Scores',
            },
        ),
        migrations.CreateModel(
            name='PHEScores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Physical & Health Education Scores')),
            ],
            options={
                'verbose_name_plural': 'PHE Scores',
            },
        ),
        migrations.CreateModel(
            name='QuantitativeReasoningScores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Quantitative Reasoning Scores')),
            ],
            options={
                'verbose_name_plural': 'Quantitative Reasoning Scores',
            },
        ),
        migrations.CreateModel(
            name='SpellingsScores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Spellings Scores')),
            ],
            options={
                'verbose_name_plural': 'Spellings Scores',
            },
        ),
        migrations.CreateModel(
            name='VerbalReasoningScores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Verbal Reasoning Scores')),
            ],
            options={
                'verbose_name_plural': 'Verbal Reasoning Scores',
            },
        ),
        migrations.RenameModel(
            old_name='BasicSciTech',
            new_name='BasicSciTechScores',
        ),
        migrations.RenameModel(
            old_name='English',
            new_name='EnglishScores',
        ),
        migrations.RenameModel(
            old_name='SocialStudies',
            new_name='SocialStudiesScores',
        ),
        migrations.DeleteModel(
            name='Abacus',
        ),
        migrations.DeleteModel(
            name='AgriculturalScience',
        ),
        migrations.DeleteModel(
            name='CivicEducation',
        ),
        migrations.DeleteModel(
            name='ComputerStudies',
        ),
        migrations.DeleteModel(
            name='CreativeArts',
        ),
        migrations.DeleteModel(
            name='CreativeWriting',
        ),
        migrations.DeleteModel(
            name='CRK',
        ),
        migrations.DeleteModel(
            name='EnglishLiterature',
        ),
        migrations.DeleteModel(
            name='History',
        ),
        migrations.DeleteModel(
            name='Music',
        ),
        migrations.DeleteModel(
            name='PHE',
        ),
        migrations.DeleteModel(
            name='QuantitativeReasoning',
        ),
        migrations.DeleteModel(
            name='Spellings',
        ),
        migrations.DeleteModel(
            name='VerbalReasoning',
        ),
        migrations.AlterModelOptions(
            name='basicscitechscores',
            options={'verbose_name_plural': 'Basic Science/Tech Scores'},
        ),
        migrations.AlterModelOptions(
            name='englishscores',
            options={'verbose_name_plural': 'English Scores'},
        ),
        migrations.AlterModelOptions(
            name='socialstudiesscores',
            options={'verbose_name_plural': 'Social Studies Scores'},
        ),
        migrations.AlterField(
            model_name='mathematicsscores',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Mathematics Scores'),
        ),
    ]
