# Generated by Django 4.2.8 on 2023-12-08 18:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('App_Quiz', '0002_questions_remove_question_exam_remove_student_user_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exam',
            options={'ordering': ('-upload_date',)},
        ),
        migrations.AddField(
            model_name='exam',
            name='upload_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
