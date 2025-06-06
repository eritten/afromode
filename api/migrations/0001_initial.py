# Generated by Django 5.2.1 on 2025-05-26 09:15

import api.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='SponsorshipApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('telephone_number', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('applied_on', models.DateTimeField(auto_now_add=True)),
                ('stage_name', models.CharField(max_length=250)),
                ('age', models.PositiveIntegerField()),
                ('talent', models.CharField(max_length=250)),
                ('about_you', models.CharField(max_length=250)),
                ('ig_handle', models.CharField(blank=True, max_length=250, null=True)),
                ('x_handle', models.CharField(blank=True, max_length=250, null=True)),
                ('youtube_handle', models.CharField(blank=True, max_length=250, null=True)),
                ('ticktock_handle', models.CharField(blank=True, max_length=250, null=True)),
                ('link_to_work', models.URLField(blank=True, null=True)),
                ('sample_project_file', models.FileField(upload_to='samples/', validators=[api.validators.validate_image_size])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TalentCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.ImageField(upload_to='images/', validators=[api.validators.validate_image_size])),
            ],
        ),
        migrations.CreateModel(
            name='TourAnnouncement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('upcoming', 'upcoming'), ('completed', 'completed')], default='upcoming', max_length=100)),
                ('description', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('currency', models.CharField(choices=[('USD', 'US Dollar'), ('EUR', 'Euro'), ('GHS', 'Ghanaian Cedi'), ('GBP', 'British Pound'), ('NGN', 'Nigerian Naira'), ('JPY', 'Japanese Yen'), ('CAD', 'Canadian Dollar'), ('AUD', 'Australian Dollar'), ('CHF', 'Swiss Franc'), ('CNY', 'Chinese Yuan'), ('INR', 'Indian Rupee')], max_length=3)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', validators=[api.validators.validate_image_size])),
            ],
        ),
        migrations.CreateModel(
            name='TourApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('telephone_number', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('applied_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dayte_to_be_performed', models.DateField(blank=True, null=True)),
                ('venue', models.CharField(blank=True, max_length=100, null=True)),
                ('activity_image', models.ImageField(upload_to='images/', validators=[api.validators.validate_image_size])),
                ('tour_announcement', models.ManyToManyField(related_name='activities', to='api.tourannouncement')),
            ],
        ),
        migrations.CreateModel(
            name='ArteeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('talent', models.CharField(max_length=250)),
                ('bio', models.TextField()),
                ('image', models.ImageField(upload_to='images/', validators=[api.validators.validate_image_size])),
                ('social_media_links', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artee_details', to='api.socialmedialinks')),
                ('talent_category', models.ManyToManyField(related_name='artee_details', to='api.talentcategory')),
                ('works', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artee_details', to='api.work')),
            ],
        ),
    ]
