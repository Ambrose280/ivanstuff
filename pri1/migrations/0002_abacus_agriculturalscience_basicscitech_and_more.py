# Generated by Django 5.0.3 on 2024-06-06 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pri1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abacus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Abacus')),
            ],
        ),
        migrations.CreateModel(
            name='AgriculturalScience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Agricultural Science')),
            ],
        ),
        migrations.CreateModel(
            name='BasicSciTech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Basic Science & Tech')),
            ],
        ),
        migrations.CreateModel(
            name='CivicEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Civic Education')),
            ],
        ),
        migrations.CreateModel(
            name='ComputerStudies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Computer Studies')),
            ],
        ),
        migrations.CreateModel(
            name='CreativeArts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Creative Arts')),
            ],
        ),
        migrations.CreateModel(
            name='CreativeWriting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Creative Handwriting')),
            ],
        ),
        migrations.CreateModel(
            name='CRK',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Christian Religious Knowledge')),
            ],
        ),
        migrations.CreateModel(
            name='English',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='English Language')),
            ],
        ),
        migrations.CreateModel(
            name='EnglishLiterature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Literature-In-English')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='History')),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Music')),
            ],
        ),
        migrations.CreateModel(
            name='PHE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Physical & Health Education')),
            ],
        ),
        migrations.CreateModel(
            name='QuantitativeReasoning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Quantitative Reasoning')),
            ],
        ),
        migrations.CreateModel(
            name='SocialStudies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Social Studies')),
            ],
        ),
        migrations.CreateModel(
            name='Spellings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Spellings')),
            ],
        ),
        migrations.CreateModel(
            name='VerbalReasoning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Verbal Reasoning')),
            ],
        ),
    ]
