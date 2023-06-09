# Generated by Django 4.1.3 on 2023-03-21 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("UCoE", "0020_remove_attendancereport_attendance_id_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student_Result",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("assignment_marks", models.IntegerField()),
                ("exam_marks", models.IntegerField()),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now_add=True)),
                (
                    "student_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="UCoE.student"
                    ),
                ),
                (
                    "subject_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="UCoE.subject"
                    ),
                ),
            ],
        ),
    ]
