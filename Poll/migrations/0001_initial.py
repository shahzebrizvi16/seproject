# Generated by Django 3.0.5 on 2020-05-09 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('ans_one', models.CharField(max_length=30)),
                ('ans_two', models.CharField(max_length=30)),
                ('ans_three', models.CharField(max_length=30)),
                ('ans_one_votes', models.IntegerField(default=0)),
                ('ans_two_votes', models.IntegerField(default=0)),
                ('ans_three_votes', models.IntegerField(default=0)),
            ],
        ),
    ]
