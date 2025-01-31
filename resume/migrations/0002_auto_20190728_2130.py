# Generated by Django 2.1.7 on 2019-07-29 01:30

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='is_current',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='club',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='club',
            name='role_description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='education',
            name='clubs',
            field=models.ManyToManyField(blank=True, to='resume.Club'),
        ),
        migrations.AlterField(
            model_name='education',
            name='courses',
            field=models.ManyToManyField(blank=True, to='resume.Course'),
        ),
        migrations.AlterField(
            model_name='education',
            name='major_gpa',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='overall_gpa',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(blank=True, verbose_name='end_date'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_date',
            field=models.DateField(blank=True, verbose_name='start_date'),
        ),
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='email_address',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='person',
            name='linkedin',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='person',
            name='state',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='zipcode',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='project',
            name='demonstrated_skill',
            field=models.ManyToManyField(blank=True, to='resume.Skill'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='github_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='education',
            field=models.ManyToManyField(blank=True, to='resume.Education'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='experience',
            field=models.ManyToManyField(blank=True, to='resume.Experience'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='overview',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='resume',
            name='projects',
            field=models.ManyToManyField(blank=True, to='resume.Project'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='skills',
            field=models.ManyToManyField(blank=True, to='resume.Skill'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
