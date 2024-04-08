# Generated by Django 4.2.11 on 2024-04-08 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_projectmembership_unique_together'),
        ('issues', '0014_alter_issue_events_at_alter_issue_fixed_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='hash',
        ),
        migrations.CreateModel(
            name='Grouping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grouping_key', models.TextField()),
                ('issue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='issues.issue')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.project')),
            ],
        ),
    ]
