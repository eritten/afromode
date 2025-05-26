# admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import (
    TalentCategory,
    SocialMediaLinks,
    Work,
    ArteeDetails,
    TourAnnouncement,
    Activity,
    SponsorshipApplication,
    TourApplication,
)


@admin.register(TalentCategory)
class TalentCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_preview')
    search_fields = ('name',)

    def icon_preview(self, obj):
        if obj.icon:
            return format_html(
                '<img src="{}" style="width:50px;height:50px;object-fit:cover;border-radius:4px;"/>',
                obj.icon.url
            )
        return "No Image"
    icon_preview.short_description = "Icon Preview"


@admin.register(SocialMediaLinks)
class SocialMediaLinksAdmin(admin.ModelAdmin):
    list_display = ('url', 'artee_count')
    search_fields = ('url',)

    def artee_count(self, obj):
        return obj.artee_details.count()
    artee_count.short_description = "Connected Artees"


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'artee_count')
    search_fields = ('title',)
    list_filter = ('title',)

    def artee_count(self, obj):
        return obj.artee_details.count()
    artee_count.short_description = "Connected Artees"


class TalentCategoryInline(admin.TabularInline):
    model = ArteeDetails.talent_category.through
    extra = 1


@admin.register(ArteeDetails)
class ArteeDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'talent', 'image_preview', 'category_list', 'social_media_links', 'works'
    )
    list_filter = ('talent_category', 'talent')
    search_fields = ('name', 'talent', 'bio')
    filter_horizontal = ('talent_category',)

    fieldsets = (
        ('Basic Information', {'fields': ('name', 'talent', 'bio', 'image')}),
        ('Social Media & Work', {'fields': ('social_media_links', 'works')}),
        ('Categories', {'fields': ('talent_category',)}),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:50px;height:50px;object-fit:cover;border-radius:50%;"/>',
                obj.image.url
            )
        return "No Image"
    image_preview.short_description = "Profile Picture"

    def category_list(self, obj):
        return ", ".join(c.name for c in obj.talent_category.all())
    category_list.short_description = "Categories"


@admin.register(TourAnnouncement)
class TourAnnouncementAdmin(admin.ModelAdmin):
    list_display = (
        'caption', 'location', 'status', 'formatted_amount', 'currency', 'activities_count', 'image_preview'
    )
    list_filter = ('status', 'currency', 'location')
    search_fields = ('caption', 'location', 'description')
    list_editable = ('status',)

    fieldsets = (
        ('Basic Information', {'fields': ('caption', 'location', 'status', 'description')}),
        ('Financial Details', {'fields': ('amount', 'currency')}),
        ('Media', {'fields': ('image',)}),
    )

    def formatted_amount(self, obj):
        return f"{obj.amount:,.2f}"
    formatted_amount.short_description = "Amount"
    formatted_amount.admin_order_field = 'amount'

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:50px;height:50px;object-fit:cover;border-radius:4px;"/>',
                obj.image.url
            )
        return "No Image"
    image_preview.short_description = "Image Preview"

    def activities_count(self, obj):
        return obj.activities.count()
    activities_count.short_description = "Activities"


class TourAnnouncementInline(admin.TabularInline):
    model = Activity.tour_announcement.through
    extra = 1


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'dayte_to_be_performed', 'venue', 'image_preview', 'tours_count')
    list_filter = ('dayte_to_be_performed', 'venue')
    search_fields = ('name', 'venue')
    date_hierarchy = 'dayte_to_be_performed'
    filter_horizontal = ('tour_announcement',)

    fieldsets = (
        ('Activity Details', {'fields': ('name', 'dayte_to_be_performed', 'venue')}),
        ('Media', {'fields': ('activity_image',)}),
        ('Tour Announcements', {'fields': ('tour_announcement',)}),
    )

    def image_preview(self, obj):
        if obj.activity_image:
            return format_html(
                '<img src="{}" style="width:50px;height:50px;object-fit:cover;border-radius:4px;"/>',
                obj.activity_image.url
            )
        return "No Image"
    image_preview.short_description = "Activity Image"

    def tours_count(self, obj):
        return obj.tour_announcement.count()
    tours_count.short_description = "Tours"


@admin.register(SponsorshipApplication)
class SponsorshipApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'stage_name', 'name', 'email', 'age', 'talent', 'applied_on', 'has_sample_file'
    )
    list_filter = ('applied_on', 'talent', 'age')
    search_fields = ('name', 'stage_name', 'email', 'talent')
    readonly_fields = ('applied_on',)
    date_hierarchy = 'applied_on'

    fieldsets = (
        ('Personal Information', {'fields': ('name', 'stage_name', 'age', 'telephone_number', 'email')}),
        ('Talent Information', {'fields': ('talent', 'about_you', 'link_to_work', 'sample_project_file')}),
        ('Social Media Handles', {'fields': ('ig_handle', 'x_handle', 'youtube_handle', 'ticktock_handle'), 'classes': ('collapse',)}),
        ('Application Details', {'fields': ('applied_on',)}),
    )

    def has_sample_file(self, obj):
        return bool(obj.sample_project_file)
    has_sample_file.short_description = "Sample File"
    has_sample_file.boolean = True


@admin.register(TourApplication)
class TourApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'telephone_number', 'applied_on')
    list_filter = ('applied_on',)
    search_fields = ('name', 'email')
    readonly_fields = ('applied_on',)
    date_hierarchy = 'applied_on'

    fieldsets = (
        ('Applicant Information', {'fields': ('name', 'telephone_number', 'email')}),
        ('Application Details', {'fields': ('applied_on',)}),
    )
