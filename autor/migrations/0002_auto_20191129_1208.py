# Generated by Django 2.2.7 on 2019-11-29 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='ocupacao_2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='autor',
            name='ocupacao',
            field=models.CharField(choices=[('Estudante', 'Estudante'), ('Professor', 'Professor'), ('Pesquisador', 'Pesquisador'), ('Entusiasta', 'Entusiasta'), ('Outro', 'Outro')], default='', max_length=50),
        ),
    ]
