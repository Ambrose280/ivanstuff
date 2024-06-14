# Generated by Django 5.0.3 on 2024-06-09 21:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pri2', '0004_remove_basicscitechscores_title_and_more'),
        ('pupilbase', '0002_pupil_address_pupil_classlevel_pupil_gender'),
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
            model_name='phescores',
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
        migrations.AlterField(
            model_name='abacusscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p2abacuspupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='agriculturalsciencescores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p2agricpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='basicscitechscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p2scitechpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='civiceducationscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p2civicpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='computerstudiesscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p2cspupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='creativeartsscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p2artspupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='creativewritingscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p2writingpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='crkscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p2crkpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='englishliteraturescores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p2literaturepupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='englishscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p2engpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='historyscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p2historypupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='mathematicsscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p2mathpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='musicscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p2musicpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='phescores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p2phepupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='quantitativereasoningscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p2quantpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='socialstudiesscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p2socialpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='spellingsscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p2spellingpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
        migrations.AlterField(
            model_name='verbalreasoningscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p2verbalpupil', to='pupilbase.pupil', verbose_name='Pupil'),
        ),
    ]
