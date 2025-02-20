# Generated by Django 4.2.18 on 2025-01-29 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparepart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sparepart',
            name='category',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='sparepart',
            name='condition',
            field=models.CharField(blank=True, choices=[('NEW', 'New'), ('USED', 'Used'), ('REFURBISHED', 'Refurbished')], max_length=50),
        ),
        migrations.AddField(
            model_name='sparepart',
            name='part_number',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='sparepart',
            name='year_end',
            field=models.IntegerField(blank=True, help_text='End year for compatibility range', null=True),
        ),
        migrations.AddIndex(
            model_name='sparepart',
            index=models.Index(fields=['year'], name='sparepart_s_year_3e083a_idx'),
        ),
        migrations.AddIndex(
            model_name='sparepart',
            index=models.Index(fields=['make', 'model'], name='sparepart_s_make_c9589e_idx'),
        ),
        migrations.AddIndex(
            model_name='sparepart',
            index=models.Index(fields=['created_at'], name='sparepart_s_created_f12a81_idx'),
        ),
    ]
