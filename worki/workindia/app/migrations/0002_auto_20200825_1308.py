# Generated by Django 3.1 on 2020-08-25 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snippet',
            options={'ordering': ['due_date']},
        ),
        migrations.RenameField(
            model_name='snippet',
            old_name='created',
            new_name='due_date',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='code',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='language',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='linenos',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='style',
        ),
        migrations.AddField(
            model_name='snippet',
            name='category',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snippet',
            name='description',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
