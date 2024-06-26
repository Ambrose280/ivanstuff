# Generated by Django 5.0.3 on 2024-06-09 21:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pri5', '0004_remove_abacusscores_title_and_more'),
        ('pupilbase', '0002_pupil_address_pupil_classlevel_pupil_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abacusscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p5abacuspupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='agriculturalsciencescores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p5agricpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='basicscitechscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p5scitechpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='civiceducationscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p5civicpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='computerstudiesscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p5cspupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='creativeartsscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p5artspupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='creativewritingscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p5writingpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='crkscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p5crkpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='englishliteraturescores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p5literaturepupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='englishscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p5engpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='historyscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p5historypupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='mathematicsscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p5mathpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='musicscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p5musicpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='phescores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p5phepupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='quantitativereasoningscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p5quantpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='socialstudiesscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p5socialpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='spellingsscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p5spellingpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='verbalreasoningscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p5verbalpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
    ]
