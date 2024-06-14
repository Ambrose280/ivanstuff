# Generated by Django 5.0.3 on 2024-06-09 21:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pri1', '0006_remove_abacusscores_title_and_more'),
        ('pupilbase', '0002_pupil_address_pupil_classlevel_pupil_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abacusscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p1abacuspupil', to='pupilbase.pupil', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='agriculturalsciencescores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p1agricpupil', to='pupilbase.pupil', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='basicscitechscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p1scitechpupil', to='pupilbase.pupil', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='civiceducationscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p1civicpupil', to='pupilbase.pupil', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='computerstudiesscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p1cspupil', to='pupilbase.pupil', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='creativeartsscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p1artspupil', to='pupilbase.pupil', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='creativewritingscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p1writingpupil', to='pupilbase.pupil', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='crkscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p1crkpupil', to='pupilbase.pupil', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='englishliteraturescores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p1literaturepupil', to='pupilbase.pupil', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='englishscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p1engpupil', to='pupilbase.pupil', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='historyscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p1historypupil', to='pupilbase.pupil', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='mathematicsscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p1mathpupil', to='pupilbase.pupil', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='musicscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p1musicpupil', to='pupilbase.pupil', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='phescores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p1phepupil', to='pupilbase.pupil', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='quantitativereasoningscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p1quantpupil', to='pupilbase.pupil', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='socialstudiesscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p1socialpupil', to='pupilbase.pupil', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='spellingsscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p1spellingpupil', to='pupilbase.pupil', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='verbalreasoningscores',
            name='pupil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p1verbalpupil', to='pupilbase.pupil', verbose_name='User'),
        ),
    ]
