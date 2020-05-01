# Generated by Django 3.0.3 on 2020-04-27 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_auto_20200427_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='credential',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='application',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='application',
            name='firstName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='interest',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='application',
            name='lastName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='reference',
            field=models.CharField(max_length=50),
        ),
    ]