# Generated by Django 5.1.1 on 2024-09-08 10:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0002_alter_chapter_subject'),
        ('subjects', '0006_remove_subjects_class_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subchapter',
            name='chapter',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='sub_chapter',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.AddField(
            model_name='exercise',
            name='chapter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='chapters.chapter'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='chapter_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='subjects.subjects'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='exercise_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='SubChapter',
        ),
    ]
