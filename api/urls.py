from django.urls import path
from .views import (
    TalentCategoryList,
    ArteesByCategoryView,
    ContactView,
    SponsorshipApplicationCreateView,
    TourAnnouncementList,
    ListArtee,
)

urlpatterns = [
    path('categories/', TalentCategoryList.as_view(), name='category-list'),
    path('categories/<int:category_id>/artees/', ArteesByCategoryView.as_view(), name='artees-by-category'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('sponsorship/', SponsorshipApplicationCreateView.as_view(), name='sponsorship-apply'),
    path('tour-news/', TourAnnouncementList.as_view(), name='tour-announcement-list'),
    path('creators/', ListArtee.as_view(), name='creators-list'),
]
