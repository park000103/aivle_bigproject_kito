# Generated by Django 5.0.6 on 2024-07-05 01:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("consultations", "0002_alter_consultation_options_and_more"),
        ("doctors", "0003_alter_doctor_options_alter_doctor_departments_id_and_more"),
        ("patients", "0002_alter_patient_options_alter_patient_patient_bday_and_more"),
        ("prescriptions", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="prescription",
            options={"verbose_name": "처방", "verbose_name_plural": "처방"},
        ),
        migrations.AlterField(
            model_name="prescription",
            name="consultation_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="consultations.consultation",
                verbose_name="진료",
            ),
        ),
        migrations.AlterField(
            model_name="prescription",
            name="doctor_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="doctors.doctor",
                verbose_name="의사",
            ),
        ),
        migrations.AlterField(
            model_name="prescription",
            name="patient_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="patients.patient",
                verbose_name="환자",
            ),
        ),
        migrations.AlterField(
            model_name="prescription",
            name="prescription_image",
            field=models.ImageField(upload_to="images/", verbose_name="처방전"),
        ),
    ]
