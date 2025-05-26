from rest_framework import serializers
from .models import TalentCategory, Work, SocialMediaLinks, ArteeDetails, SponsorshipApplication, TourAnnouncement, \
    Activity


class WorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['id', 'title', 'link']


class SocialMediaLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLinks
        fields = ['id', 'url']


class ArteDetailsSerializer(serializers.ModelSerializer):
    works = serializers.SerializerMethodField()
    social_media_links = serializers.SerializerMethodField()

    class Meta:
        model = ArteeDetails
        fields = [
            'id', 'name', 'talent', 'bio', 'image',
            'social_media_links', 'works'
        ]

    def get_works(self, obj):
        """Return works as array"""
        if obj.works:
            return [WorksSerializer(obj.works).data]
        return []

    def get_social_media_links(self, obj):
        """Return social media links as array"""
        if obj.social_media_links:
            return [SocialMediaLinksSerializer(obj.social_media_links).data]
        return []


class TalentCategorySerializer(serializers.ModelSerializer):
#    artee_details = ArteDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = TalentCategory
        fields = ['id', 'name', 'icon']


class ContactSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    message = serializers.CharField()


class SponsorshipApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorshipApplication
        fields = [
            "name",  # inherited from AbstractApplication
            'telephone_number',
            "email",
            "age",
            "talent",
            "about_you",
            "ig_handle",
            "x_handle",
            "youtube_handle",
            "ticktock_handle",
            "link_to_work",
            "sample_project_file",
        ]

    def validate_age(self, value):
        if value < 16:
            raise serializers.ValidationError("You must be at least 16 years old to apply.")
        return value

    def validate_about_you(self, value):
        if len(value.strip()) < 20:
            raise serializers.ValidationError("Please tell us more about yourself (at least 20 characters).")
        return value


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'name', 'dayte_to_be_performed', 'venue', 'activity_image']
        read_only_fields = ['id']


class TourAnnouncementSerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(many=True, read_only=True)

    class Meta:
        model = TourAnnouncement
        fields = [
            'id',
            'caption',
            'location',
            'status',
            'description',
            'amount',
            'currency',
            'image',
            'activities',
        ]
        read_only_fields = ['id']
