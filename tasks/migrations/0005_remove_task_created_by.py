# Generated by Django 2.2.5 on 2019-09-28 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("tasks", "0004_auto_20190926_1943")]

    operations = [migrations.RemoveField(model_name="task", name="created_by")]
