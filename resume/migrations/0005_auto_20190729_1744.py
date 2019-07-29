# Generated by Django 2.1.7 on 2019-07-29 21:44

from django.db import migrations
import partial_date.fields


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20190729_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='expected_end_year',
            field=partial_date.fields.PartialDateField(blank=True, null=True, verbose_name='expected_end_year'),
        ),
        migrations.AlterField(
            model_name='education',
            name='year_ended',
            field=partial_date.fields.PartialDateField(blank=True, null=True, verbose_name='end_year'),
        ),
        migrations.AlterField(
            model_name='education',
            name='year_started',
            field=partial_date.fields.PartialDateField(blank=True, null=True, verbose_name='start_year'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, verbose_name='end_date'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_date',
            field=partial_date.fields.PartialDateField(blank=True, verbose_name='start_date'),
        ),
    ]