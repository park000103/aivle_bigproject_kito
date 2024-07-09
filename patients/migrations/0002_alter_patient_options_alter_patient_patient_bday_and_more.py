# Generated by Django 5.0.6 on 2024-07-05 01:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("patients", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="patient",
            options={"verbose_name": "환자", "verbose_name_plural": "환자"},
        ),
        migrations.AlterField(
            model_name="patient",
            name="patient_bday",
            field=models.CharField(
                blank=True, max_length=6, verbose_name="생년월일(YYMMDD)"
            ),
        ),
        migrations.AlterField(
            model_name="patient",
            name="patient_birth",
            field=models.DateField(verbose_name="생년월일"),
        ),
        migrations.AlterField(
            model_name="patient",
            name="patient_name",
            field=models.CharField(max_length=200, verbose_name="환자 이름"),
        ),
    ]