# Generated by Django 5.0.3 on 2024-06-09 21:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pri3', '0004_remove_agriculturalsciencescores_title_and_more'),
        ('pupilbase', '0002_pupil_address_pupil_classlevel_pupil_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creativewritingscores',
            name='title',
        ),
        migrations.AlterField(
            model_name='abacusscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p3abacuspupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='agriculturalsciencescores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p3agricpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='basicscitechscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p3scitechpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='civiceducationscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p3civicpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='computerstudiesscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p3cspupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='creativeartsscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p3artspupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='creativewritingscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p3writingpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='crkscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p3crkpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='englishliteraturescores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p3literaturepupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='englishscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p3engpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='historyscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p3historypupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='mathematicsscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p3mathpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='musicscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p3musicpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='phescores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p3phepupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='quantitativereasoningscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p3quantpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='socialstudiesscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p3socialpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='spellingsscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p3spellingpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='verbalreasoningscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p3verbalpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
    ]
