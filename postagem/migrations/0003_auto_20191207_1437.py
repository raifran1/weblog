# Generated by Django 2.2.7 on 2019-12-07 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postagem', '0002_auto_20191207_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postagem',
            name='dt_criacao',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='postagem',
            name='dt_publicacao',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
