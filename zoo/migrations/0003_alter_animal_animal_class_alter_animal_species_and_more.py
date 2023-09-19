# Generated by Django 4.2.5 on 2023-09-19 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0002_animalclass_animalspecies_employeeposition_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='animal_class',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='zoo.animalclass'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='species',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='zoo.animalspecies'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='zoo.employeeposition'),
        ),
    ]
