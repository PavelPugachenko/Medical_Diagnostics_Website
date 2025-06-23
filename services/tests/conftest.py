import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from services.models import Service, Feedback
from django.test import Client


@pytest.fixture
def sample_service():
    return Service.objects.create(
        title="Test Service",
        description="Test Description",
        price=99.99,
        image=SimpleUploadedFile("../../media/services/images.png", b"file_content", content_type="image/jpeg")
    )

@pytest.fixture
def feedback_data():
    return {
        'name': 'Test User',
        'email': 'test@example.com',
        'message': 'Test message'
    }


@pytest.fixture
def client():
    return Client()

@pytest.fixture
def service():
    return Service.objects.create(
        title="Стоматология",
        description="Лечение зубов",
        price=5000
    )