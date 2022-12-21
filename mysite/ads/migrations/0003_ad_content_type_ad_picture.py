# Generated by Django 4.0.6 on 2022-11-06 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_auto_20221025_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='content_type',
            field=models.CharField(help_text='The MIMEType of the file', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='ad',
            name='picture',
            field=models.BinaryField(editable=True, null=True),
        ),
    ]
