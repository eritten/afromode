from django.core.exceptions import ValidationError


def validate_image_size(image):
    max_size_image_size = 2 * 1024 * 1024
    if image.size > max_size_image_size:
        raise ValidationError("Image too large")
