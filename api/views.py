# views.py
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView

from .models import TalentCategory, SponsorshipApplication, TourAnnouncement, ArteeDetails
from .serializers import (
    TalentCategorySerializer,
    ContactSerializer,
    SponsorshipApplicationCreateSerializer, TourAnnouncementSerializer,
ArteDetailsSerializer
)


class TalentCategoryList(generics.ListAPIView):
    queryset = TalentCategory.objects.prefetch_related("artee_details").all()
    serializer_class = TalentCategorySerializer


class ContactView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        # Render subject & body from templates (you’ll need to create these under templates/mail/)
        subject = render_to_string("mail/contact_subject.txt", data).strip()
        text_body = render_to_string("mail/contact_body.txt", data)

        # Prepare email
        email = EmailMultiAlternatives(
            subject=subject,
            body=text_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.DEFAULT_FROM_EMAIL],  # or your support/admin address
            reply_to=[data.get("email")],  # so replies go back to the sender
        )
        # Send it
        email.send(fail_silently=False)
        return Response({"message": "Email sent."}, status=status.HTTP_200_OK)


class SponsorshipApplicationCreateView(CreateAPIView):
    """
    API view to handle creation of SponsorshipApplication instances.
    Uses the SponsorshipApplicationCreateSerializer to validate and save data,
    then sends a notification email upon successful creation.
    """
    queryset = SponsorshipApplication.objects.all()
    serializer_class = SponsorshipApplicationCreateSerializer

    def create(self, request, *args, **kwargs):
        # Validate and save application
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        application = serializer.save()

        # Prepare email context
        context = {
            'name': application.name,
            'stage_name': application.stage_name,
            'email': application.email if hasattr(application, 'email') else None,
            'talent': application.talent,
        }

        # Render email templates
        subject = render_to_string("mail/sponsorship_subject.txt", context).strip()
        text_body = render_to_string("mail/sponsorship_body.txt", context)

        # Send notification to admins or a designated address
        notification_email = EmailMultiAlternatives(
            subject=subject,
            body=text_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.DEFAULT_FROM_EMAIL],
        )
        notification_email.send(fail_silently=False)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TourAnnouncementList(generics.ListAPIView):
    queryset = TourAnnouncement.objects.prefetch_related("activities").all()
    serializer_class = TourAnnouncementSerializer


class ArteesByCategoryView(generics.ListAPIView):
    """
    Returns all ArteeDetails for a given talent category.
    Expects 'category_id' as a URL parameter.
    """
    serializer_class = ArteDetailsSerializer

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return ArteeDetails.objects.filter(talent_category__id=category_id)
