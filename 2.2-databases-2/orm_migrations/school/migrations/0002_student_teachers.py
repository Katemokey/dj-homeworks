from django.db import migrations, models


def copy_teacher_to_teachers(apps, schema_editor):
    Student = apps.get_model('school', 'Student')
    for student in Student.objects.all():
        student.teachers.add(student.teacher_id)


def copy_teachers_to_teacher(apps, schema_editor):
    Student = apps.get_model('school', 'Student')
    for student in Student.objects.all():
        teacher = student.teachers.first()
        if teacher is not None:
            student.teacher = teacher
            student.save(update_fields=['teacher'])


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(
                related_name='students',
                to='school.teacher',
                verbose_name='Учителя',
            ),
        ),
        migrations.RunPython(
            copy_teacher_to_teachers,
            copy_teachers_to_teacher,
        ),
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
    ]
