# Generated by Django 3.0.6 on 2020-07-20 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Enquiry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='Batch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Enquiry.Batch'),
            preserve_default=False,
        ),
    ]
