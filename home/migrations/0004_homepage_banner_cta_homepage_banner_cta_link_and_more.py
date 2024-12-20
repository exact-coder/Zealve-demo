# Generated by Django 5.1.3 on 2024-11-12 07:44

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_banner'),
        ('wagtailcore', '0094_alter_page_locale'),
        ('wagtailimages', '0027_image_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner_cta',
            field=models.CharField(default=django.utils.timezone.now, help_text='Text to display on Call to Action', max_length=50, verbose_name=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner_cta_link',
            field=models.ForeignKey(blank=True, help_text='Choose a page to link to for the Call to Action', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='homePageBannerLink', to='wagtailcore.page'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner_cta_url',
            field=models.URLField(blank=True, help_text='if banner_cta_link not found. Then this url will work', max_length=250, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner_subtitle',
            field=models.CharField(blank=True, help_text='Banner Subtitle ', max_length=300, null=True, verbose_name='Banner Sub Title'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner_title',
            field=models.CharField(default=datetime.datetime(2024, 11, 12, 7, 44, 14, 839040, tzinfo=datetime.timezone.utc), help_text='Banner Title *', max_length=100, verbose_name='Banner Title'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Banner',
        ),
    ]
