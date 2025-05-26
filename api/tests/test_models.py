import pytest
from django.core.files.uploadedfile import SimpleUploadedFile

from api.models import ArtVideoPost, ArtPhotoPost

@pytest.mark.django_db
class TestModels:

    @pytest.fixture
    def video_data(self):
        return {
            "artee_name": "eritten",
            "biography": "test bio",
            "type_of_genre": "hiphop",
            "video_url": "http://test.com"
        }

    @pytest.fixture
    def photo_data(self):
        # create a 1KB dummy PNG
        return {
            "artee_name": "eritten",
            "biography": "test bio",
            "type_of_genre": "hiphop",
            "image": "test.png"
        }

    def test_instantiate_art_video_post(self, video_data):
        post = ArtVideoPost(**video_data)
        assert post.artee_name == video_data["artee_name"]
        assert post.biography == video_data["biography"]
        assert post.type_of_genre == video_data["type_of_genre"]
        assert post.video_url == video_data["video_url"]

    def test_save_and_retrieve_art_video_post(self, video_data):
        post = ArtVideoPost.objects.create(**video_data)
        fetched = ArtVideoPost.objects.get(pk=post.pk)
        for field in ("artee_name", "biography", "type_of_genre", "video_url"):
            assert getattr(fetched, field) == video_data[field]

    def test_instantiate_and_save_art_photo_post(self, photo_data):
        post = ArtPhotoPost.objects.create(**photo_data)
        fetched = ArtPhotoPost.objects.get(pk=post.pk)
        assert fetched.artee_name == photo_data["artee_name"]
        # the stored file name should match
        assert fetched.image.name.endswith("test.png")
