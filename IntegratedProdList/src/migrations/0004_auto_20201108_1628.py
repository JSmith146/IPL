# Generated by Django 2.2 on 2020-11-08 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0003_auto_20201107_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_lead',
            field=models.CharField(choices=[('SMITH, JEFF', 'SMITH, JEFF'), ('STARK, TONY', 'STARK, TONY'), ('RODGERS, STEVE', 'RODGERS, STEVE'), ('WAYNE, BRUCE', 'WAYNE, BRUCE'), ('PARKER, PETER', 'PARKER, PETER'), ('KENT, CLARK', 'KENT, CLARK'), ('CYBORG-MAN, VISION', 'CYBORG-MAN, VISION'), ('BARTON, CLINT', 'BARTON, CLINT'), ('ROMANOFF, NATASHA', 'ROMANOFF, NATASHA')], max_length=100),
        ),
    ]
