# Generated by Django 3.2.9 on 2021-12-04 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_userdetail_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='email',
            field=models.EmailField(default=1, max_length=155),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdetail',
            name='place',
            field=models.CharField(default=1, max_length=155),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='age',
            field=models.IntegerField(),
        ),
    ]
