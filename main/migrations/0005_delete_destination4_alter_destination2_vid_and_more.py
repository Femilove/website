# Generated by Django 5.1.2 on 2024-10-28 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_destination2_vid_alter_destination3_vid_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Destination4',
        ),
        migrations.AlterField(
            model_name='destination2',
            name='vid',
            field=models.FileField(upload_to='videos_uploaded'),
        ),
        migrations.AlterField(
            model_name='destination3',
            name='vid',
            field=models.FileField(upload_to='videos_uploaded'),
        ),
    ]
