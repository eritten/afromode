from django.db import models
from .validators import validate_image_size


# Create your models here.

class TalentCategory(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='images/', validators=[validate_image_size])

    def __str__(self):
        return self.name


class SocialMediaLinks(models.Model):
    url = models.URLField()


class Work(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.title


class ArteeDetails(models.Model):
    name = models.CharField(max_length=100)
    talent = models.CharField(max_length=250)
    bio = models.TextField()
    image = models.ImageField(upload_to='images/', validators=[validate_image_size])
    social_media_links = models.ForeignKey(SocialMediaLinks, on_delete=models.CASCADE, related_name='artee_details',
                                           blank=True, null=True)
    talent_category = models.ManyToManyField(TalentCategory, related_name='artee_details')
    works = models.ForeignKey(Work, related_name='artee_details', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class TourAnnouncement(models.Model):
    CURRENCY_TYPES = (
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('GHS', 'Ghanaian Cedi'),
        ('GBP', 'British Pound'),
        ('NGN', 'Nigerian Naira'),
        ('JPY', 'Japanese Yen'),
        ('CAD', 'Canadian Dollar'),
        ('AUD', 'Australian Dollar'),
        ('CHF', 'Swiss Franc'),
        ('CNY', 'Chinese Yuan'),
        ('INR', 'Indian Rupee'),
    )
    STATUS_CHOICES = (("upcoming", "upcoming"), ("completed", "completed"))
    caption = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="upcoming")
    description = models.TextField()
    amount = models.DecimalField(decimal_places=2, max_digits=20)
    currency = models.CharField(max_length=3, choices=CURRENCY_TYPES)
    image = models.ImageField(upload_to='images/', validators=[validate_image_size], blank=True, null=True)
    event_date = models.DateField()
    def __str__(self):
        return self.caption


class Activity(models.Model):
    name = models.CharField(max_length=100)
    dayte_to_be_performed = models.DateField(blank=True, null=True)
    venue = models.CharField(max_length=100, blank=True, null=True)
    activity_image = models.ImageField(upload_to='images/', validators=[validate_image_size])
    tour_announcement = models.ManyToManyField(TourAnnouncement, related_name="activities")

    def __str__(self):
        return self.name


class AbstractApplication(models.Model):
    name = models.CharField(max_length=100)
    telephone_number = models.CharField(max_length=100)
    email = models.EmailField()
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class SponsorshipApplication(AbstractApplication):
    stage_name = models.CharField(max_length=250)
    age = models.PositiveIntegerField()
    talent = models.CharField(max_length=250)
    about_you = models.CharField(max_length=250)
    ig_handle = models.CharField(max_length=250, blank=True, null=True)
    x_handle = models.CharField(max_length=250, blank=True, null=True)
    youtube_handle = models.CharField(max_length=250, blank=True, null=True)
    ticktock_handle = models.CharField(max_length=250, blank=True, null=True)
    link_to_work = models.URLField(blank=True, null=True)
    sample_project_file = models.FileField(upload_to='samples/', validators=[validate_image_size])

    def __str__(self):
        return self.stage_name


class TourApplication(AbstractApplication):
    def __str__(self):
        return self.name
