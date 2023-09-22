# Generated by Django 4.2.5 on 2023-09-21 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades empleados',
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['id'], 'verbose_name': 'Mi empleado', 'verbose_name_plural': 'Empleados de la empresa'},
        ),
        migrations.AddField(
            model_name='empleado',
            name='habilidad',
            field=models.ManyToManyField(to='empleados.habilidades'),
        ),
    ]
